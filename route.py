#!/usr/bin/env python3
"""llm-route: escolhe o provedor/modelo de IA para uma tarefa a partir de regras em JSON (sem chamar nenhuma API)."""
import json, sys
def escolher(regras, tarefa, tokens=0):
    for r in regras["regras"]:
        if r.get("palavras") and not any(p in tarefa.lower() for p in r["palavras"]): continue
        if tokens > r.get("max_tokens", 10**9): continue
        return r["destino"]
    return regras["padrao"]
if __name__ == "__main__":
    regras = json.load(open(sys.argv[1])); print(escolher(regras, sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 0))
