from automato import Automato, EPSILON

Passo = tuple[str | None, set[str]]

def fecho_epsilon(a: Automato, estados: set[str]) -> set[str]:

    visitados = set(estados)
    pilha = list(estados)

    while pilha:
        estado = pilha.pop()
        destinos = a.transicoes.get((estado, EPSILON), set())

        for destino in destinos:
            if destino not in visitados:
                visitados.add(destino)
                pilha.append(destino)

    return visitados


def mover(a: Automato, estados: set[str], simbolo: str) -> set[str]:

    destinos = set()

    for estado in estados:
        destinos.update(a.transicoes.get((estado, simbolo), set()))

    return destinos


def processar_palavra(a: Automato, palavra: str) -> tuple[list[Passo], bool]:

    ativos = fecho_epsilon(a, {a.inicial})
    passos: list[Passo] = [(None, ativos.copy())]

    for simbolo in palavra:
        
        ativos = mover(a, ativos, simbolo)
        ativos = fecho_epsilon(a, ativos)
        passos.append((simbolo, ativos.copy()))

    aceita = bool(ativos & a.finais)

    return passos, aceita