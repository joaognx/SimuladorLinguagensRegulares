import json
from automato import Automato

def carregar_automato(caminho) -> Automato:
    with open(caminho, encoding="utf-8") as f:
        dados = json.load(f)
    transicoes = {}
    for origem, simbolo, destino in dados["transicoes"]:
        transicoes.setdefault((origem, simbolo), set()).add(destino)
    return Automato(
        estados=set(dados["estados"]),
        alfabeto=set(dados["alfabeto"]),
        inicial=dados["inicial"],
        finais=set(dados["finais"]),
        transicoes=transicoes,
        palavras=dados.get("palavras", []),
    )
