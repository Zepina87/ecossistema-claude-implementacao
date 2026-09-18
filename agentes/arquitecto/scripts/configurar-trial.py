#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
O Arquitecto — Configurador de Trial Pipedrive v2.0
Uso: python configurar-trial.py --token TOKEN --config config.json [--reset]
Novidades v2: user rename, won/lost deals, leads inbox
"""

import requests
import json
import sys
import time
import argparse
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

BASE = "https://api.pipedrive.com/v1"
SSL_VERIFY = False

def api_get(token, endpoint, params=None):
    url = f"{BASE}/{endpoint}"
    p = {"api_token": token, "limit": 100}
    if params:
        p.update(params)
    r = requests.get(url, params=p, verify=SSL_VERIFY)
    return r.json()

def api_post(token, endpoint, data):
    url = f"{BASE}/{endpoint}"
    r = requests.post(url, params={"api_token": token}, json=data, verify=SSL_VERIFY)
    try:
        result = r.json()
        if not result.get("success"):
            print(f"  [WARN] {endpoint}: {result.get('error', 'unknown error')}")
        return result
    except Exception:
        return {}

def api_put(token, endpoint, data):
    url = f"{BASE}/{endpoint}"
    r = requests.put(url, params={"api_token": token}, json=data, verify=SSL_VERIFY)
    return r.json()

def api_delete(token, endpoint):
    url = f"{BASE}/{endpoint}"
    r = requests.delete(url, params={"api_token": token}, verify=SSL_VERIFY)
    return r.json()

def log(msg):
    print(f"  -> {msg}")

# ─── RESET ──────────────────────────────────────────────────────────
def reset_trial(token):
    print("\n[RESET] A limpar trial...")

    # Apagar leads inbox
    leads = api_get(token, "leads", {"limit": 500}).get("data") or []
    for l in leads:
        api_delete(token, f"leads/{l['id']}")
    log(f"Leads apagados: {len(leads)}")
    time.sleep(0.3)

    # Apagar actividades (nao sao removidas ao apagar deals)
    acts = api_get(token, "activities", {"limit": 500}).get("data") or []
    for a in acts:
        api_delete(token, f"activities/{a['id']}")
    log(f"Actividades apagadas: {len(acts)}")
    time.sleep(0.3)

    # Apagar deals
    deals = api_get(token, "deals", {"status": "all_not_deleted"}).get("data") or []
    for d in deals:
        api_delete(token, f"deals/{d['id']}")
    log(f"Deals apagados: {len(deals)}")
    time.sleep(0.3)

    # Apagar persons
    persons = api_get(token, "persons").get("data") or []
    for p in persons:
        api_delete(token, f"persons/{p['id']}")
    log(f"Persons apagados: {len(persons)}")
    time.sleep(0.3)

    # Apagar organizations
    orgs = api_get(token, "organizations").get("data") or []
    for o in orgs:
        api_delete(token, f"organizations/{o['id']}")
    log(f"Organizacoes apagadas: {len(orgs)}")
    time.sleep(0.3)

    # Apagar stages
    stages = api_get(token, "stages").get("data") or []
    for s in stages:
        api_delete(token, f"stages/{s['id']}")
    log(f"Stages apagados: {len(stages)}")
    time.sleep(0.3)

    # Apagar custom deal fields
    # NB: campos criados via API tem add_visible_flag=false, por isso NAO exigir esse flag
    # (senao acumulam-se orfaos a cada demo). edit_flag=true isola os custom dos default.
    fields = api_get(token, "dealFields", {"limit": 500}).get("data") or []
    custom = [f for f in fields if f.get("edit_flag")]
    for f in custom:
        api_delete(token, f"dealFields/{f['id']}")
    log(f"Custom fields apagados: {len(custom)}")
    time.sleep(0.3)

    print("[RESET] Concluido.\n")

# ─── CONFIGURAR ─────────────────────────────────────────────────────
def configurar(token, config):
    empresa = config.get("empresa", "Demo")
    sector  = config.get("sector", "PME")
    print(f"\n[CONFIGURAR] {empresa} — sector: {sector}")

    # 0. Renomear utilizador
    if config.get("user_nome"):
        me = api_get(token, "users/me").get("data") or {}
        uid = me.get("id")
        if uid:
            api_put(token, f"users/{uid}", {"name": config["user_nome"]})
            log(f"Utilizador renomeado: {config['user_nome']}")
        time.sleep(0.3)

    # 1. Renomear pipeline principal
    pipelines = api_get(token, "pipelines").get("data") or []
    pipeline_id = pipelines[0]["id"] if pipelines else None
    if pipeline_id:
        nome_pipeline = config.get("pipeline_nome", f"Pipeline {empresa}")
        api_put(token, f"pipelines/{pipeline_id}", {"name": nome_pipeline})
        log(f"Pipeline renomeado: {nome_pipeline}")

    # 2. Criar stages
    stages_config = config.get("stages", [])
    stage_ids = []
    for i, stage in enumerate(stages_config):
        r = api_post(token, "stages", {
            "name": stage["name"],
            "pipeline_id": pipeline_id,
            "order_nr": i + 1,
            "deal_probability": stage.get("probabilidade", 20 + i * 15)
        })
        sid = r.get("data", {}).get("id")
        if sid:
            stage_ids.append(sid)
        log(f"Stage criado: {stage['name']}")
        time.sleep(0.2)

    # 3. Criar custom fields
    custom_fields_map = {}
    for field in config.get("custom_fields", []):
        tipo_raw = field.get("tipo", "varchar")
        tipo_api = "enum" if tipo_raw == "varchar_options" else tipo_raw
        payload = {"name": field["name"], "field_type": tipo_api}
        if field.get("opcoes") and tipo_api == "enum":
            payload["options"] = [{"label": o} for o in field["opcoes"]]
        r = api_post(token, "dealFields", payload)
        data_obj = r.get("data") or {}
        key = data_obj.get("key")
        if key:
            custom_fields_map[field["name"]] = key
        log(f"Custom field criado: {field['name']}")
        time.sleep(0.3)

    # 4. Criar organizacoes
    org_ids = {}
    for org in config.get("organizacoes", []):
        r = api_post(token, "organizations", {
            "name": org["name"],
            "address": org.get("morada", "Lisboa, Portugal")
        })
        oid = (r.get("data") or {}).get("id")
        if oid:
            org_ids[org["name"]] = oid
        log(f"Organizacao criada: {org['name']}")
        time.sleep(0.2)

    # 5. Criar persons
    person_ids = {}
    for person in config.get("persons", []):
        payload = {
            "name": person["name"],
            "phone": [{"value": person.get("phone", "+351910000000"), "primary": True}]
        }
        if person.get("email"):
            payload["email"] = [{"value": person["email"], "primary": True}]
        if person.get("org") and org_ids.get(person["org"]):
            payload["org_id"] = org_ids[person["org"]]
        r = api_post(token, "persons", payload)
        pid = (r.get("data") or {}).get("id")
        if pid:
            person_ids[person["name"]] = pid
        log(f"Person criado: {person['name']}")
        time.sleep(0.2)

    # 6. Criar deals
    deal_ids = []
    deals_config = config.get("deals", [])
    for i, deal in enumerate(deals_config):
        stage_idx = min(deal.get("stage_idx", i % max(len(stage_ids), 1)), len(stage_ids) - 1)
        payload = {
            "title": deal["title"],
            "pipeline_id": pipeline_id,
            "stage_id": stage_ids[stage_idx] if stage_ids else None,
            "value": deal.get("valor", 5000),
            "currency": "EUR",
            "status": "open"
        }
        if deal.get("expected_close_date"):
            payload["expected_close_date"] = deal["expected_close_date"]
        if deal.get("org") and org_ids.get(deal["org"]):
            payload["org_id"] = org_ids[deal["org"]]
        if deal.get("person") and person_ids.get(deal["person"]):
            payload["person_id"] = person_ids[deal["person"]]
        for nome_field, valor in deal.get("campos_custom", {}).items():
            key = custom_fields_map.get(nome_field)
            if key:
                payload[key] = valor
        r = api_post(token, "deals", payload)
        did = (r.get("data") or {}).get("id")
        if did:
            deal_ids.append(did)
            if deal.get("nota"):
                api_post(token, "notes", {"content": deal["nota"], "deal_id": did})
        log(f"Deal criado: {deal['title']}")
        time.sleep(0.3)

    # 6b. Marcar won/lost
    for i, deal in enumerate(deals_config):
        if i >= len(deal_ids):
            break
        status = deal.get("status", "open")
        if status == "won":
            api_put(token, f"deals/{deal_ids[i]}", {"status": "won"})
            log(f"Deal GANHO: {deal['title']}")
            time.sleep(0.2)
        elif status == "lost":
            api_put(token, f"deals/{deal_ids[i]}", {
                "status": "lost",
                "lost_reason": deal.get("lost_reason", "Sem motivo registado")
            })
            log(f"Deal PERDIDO: {deal['title']}")
            time.sleep(0.2)

    # 7. Criar actividades
    for act in config.get("actividades", []):
        did = deal_ids[act.get("deal_idx", 0)] if deal_ids else None
        payload = {
            "subject": act["subject"],
            "type": act.get("type", "call"),
            "due_date": act.get("due_date", "2026-05-26"),
            "due_time": act.get("due_time", "10:00"),
            "note": act.get("note", "")
        }
        if did:
            payload["deal_id"] = did
        if act.get("person") and person_ids.get(act["person"]):
            payload["person_id"] = person_ids[act["person"]]
        api_post(token, "activities", payload)
        log(f"Actividade criada: {act['subject']}")
        time.sleep(0.2)

    # 8. Criar leads inbox
    leads_count = 0
    for lead in config.get("leads_inbox", []):
        pid = person_ids.get(lead.get("person"))
        oid = org_ids.get(lead.get("org"))
        # Pipedrive exige person_id OU organization_id na lead.
        # Se a lead nao referencia nenhum existente, criar org a partir do titulo.
        if not pid and not oid:
            org_nome = lead["title"].split(" — ")[0].split(" - ")[0].strip()
            r_org = api_post(token, "organizations", {"name": org_nome})
            oid = (r_org.get("data") or {}).get("id")
            if oid:
                org_ids[org_nome] = oid
            time.sleep(0.2)
        payload = {"title": lead["title"]}
        if pid:
            payload["person_id"] = pid
        if oid:
            payload["organization_id"] = oid
        if lead.get("valor"):
            payload["value"] = {"amount": lead["valor"], "currency": "EUR"}
        if lead.get("expected_close_date"):
            payload["expected_close_date"] = lead["expected_close_date"]
        r = api_post(token, "leads", payload)
        if (r.get("data") or {}).get("id"):
            leads_count += 1
        log(f"Lead inbox: {lead['title']}")
        time.sleep(0.2)

    print(f"\n[CONCLUIDO] Trial configurado para {empresa}!")
    print(f"  Pipeline:      {config.get('pipeline_nome')}")
    print(f"  Stages:        {len(stage_ids)}")
    print(f"  Deals:         {len(deal_ids)} (open + won + lost)")
    print(f"  Leads inbox:   {leads_count}")
    print(f"  Organizacoes:  {len(org_ids)}")
    print(f"  Persons:       {len(person_ids)}")
    return {
        "pipeline_id": pipeline_id,
        "stage_ids": stage_ids,
        "deal_ids": deal_ids,
        "org_ids": org_ids,
        "person_ids": person_ids
    }

# ─── MAIN ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Configurar trial Pipedrive v2.0")
    parser.add_argument("--token", required=True)
    parser.add_argument("--config", required=True)
    parser.add_argument("--reset", action="store_true")
    args = parser.parse_args()

    with open(args.config, "r", encoding="utf-8") as f:
        config = json.load(f)

    if args.reset:
        reset_trial(args.token)

    resultado = configurar(args.token, config)
    print("\n" + json.dumps(resultado, indent=2))
