#!/usr/bin/env python3
"""Register one or more Z.ai OpenAI-compatible keys in local 9Router."""
from __future__ import annotations

import argparse
import datetime as dt
import getpass
import json
import os
import sqlite3
from pathlib import Path

DB = Path.home() / ".9router/db/data.sqlite"
BASE_URL = "https://api.z.ai/api/coding/paas/v4"
PREFIX = "zai"
NODE_ID = "openai-compatible-chat-zai"
MODELS = ("glm-4.7-flash", "glm-4.5-flash", "glm-5.2")


def keys_from_args(values: list[str] | None) -> list[str]:
    raw = values or os.getenv("ZAI_API_KEYS", "").split(",")
    keys = [key.strip() for key in raw if key.strip()]
    if not keys:
        keys = [getpass.getpass(f"Z.ai API key #{i}: ") for i in range(1, 2)]
    if any(key.startswith(("sk-", "pk-")) is False for key in keys):
        raise ValueError("Each key must look like a Z.ai API key")
    return list(dict.fromkeys(keys))


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def install(keys: list[str], db_path: Path = DB) -> None:
    if not db_path.is_file():
        raise FileNotFoundError(f"9Router database not found: {db_path}")
    node_data = {"prefix": PREFIX, "apiType": "chat", "baseUrl": BASE_URL, "nodeName": "Z.ai GLM"}
    stamp = now()
    with sqlite3.connect(db_path) as db:
        db.execute("""INSERT INTO providerNodes(id,type,name,data,createdAt,updatedAt)
            VALUES(?, 'openai-compatible', ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET data=excluded.data, updatedAt=excluded.updatedAt""",
                   (NODE_ID, "Z.ai GLM", json.dumps(node_data), stamp, stamp))
        for index, key in enumerate(keys, 1):
            conn_id = f"conn-zai-{index}"
            data = {
                "defaultModel": MODELS[0], "apiKey": key, "prefix": PREFIX,
                "apiType": "chat", "baseUrl": BASE_URL, "nodeName": "Z.ai GLM",
                "testStatus": "untested", "models": list(MODELS), "backoffLevel": 0,
                "providerSpecificData": {**node_data, "connectionProxyEnabled": False,
                                         "connectionProxyUrl": "", "connectionNoProxy": ""},
            }
            db.execute("""INSERT INTO providerConnections
                (id,provider,authType,name,email,priority,isActive,data,createdAt,updatedAt)
                VALUES(?, ?, 'apikey', ?, NULL, ?, 1, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET data=excluded.data, priority=excluded.priority,
                    isActive=1, updatedAt=excluded.updatedAt""",
                       (conn_id, NODE_ID, f"Z.ai GLM #{index}", index,
                        json.dumps(data), stamp, stamp))
        for model in MODELS:
            target = json.dumps(f"{NODE_ID}/{model}")
            for alias in (model, f"{PREFIX}/{model}", f"{PREFIX}-{model}"):
                db.execute("INSERT OR REPLACE INTO kv(scope,key,value) VALUES('modelAliases',?,?)",
                           (alias, target))
            for provider in (PREFIX, NODE_ID):
                db.execute("INSERT OR REPLACE INTO kv(scope,key,value) VALUES('customModels',?,?,?)".replace("?,?,?", "?,?"),
                           (f"{provider}|{model}|llm", json.dumps({"providerAlias": provider, "id": model, "type": "llm", "name": model})))
        db.commit()
    print(f"Registered {len(keys)} Z.ai key(s) in {db_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("keys", nargs="*", help="keys; omitted keys are read from ZAI_API_KEYS or prompt")
    args = parser.parse_args()
    install(keys_from_args(args.keys))
