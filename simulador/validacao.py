from automato import Automato, EPSILON


def validar_automato(a: Automato) -> list[str]:
    erros = []

    # regra 1: q0 precisa estar em Q
    if a.inicial not in a.estados:
        erros.append(f"Estado inicial '{a.inicial}' não pertence ao conjunto de estados Q")

    # regra 2: todo estado final precisa estar em Q
    diferenca = a.finais - a.estados
    for estado in diferenca:
        erros.append(f"Estado final '{estado}' não pertence ao conjunto de estados Q")

    # regra 3: ε não pode estar no alfabeto
    if EPSILON in a.alfabeto:
        erros.append(f"'{EPSILON}' representa ε e não pode pertencer ao alfabeto")

    # regra 4: cada símbolo de Σ deve ter exatamente 1 caractere
    # (a Pessoa 2 vai percorrer a palavra caractere por caractere)
    for simbolo in a.alfabeto:
        if len(simbolo) != 1:
            erros.append(f"Símbolo '{simbolo}' do alfabeto deve ter exatamente 1 caractere")

    # regra 5: para cada (origem, simbolo) -> destinos em a.transicoes:
    # origem ∈ Q, simbolo ∈ Σ ∪ {ε}, cada destino ∈ Q
    for (origem, simbolo), destinos in a.transicoes.items():
        if origem not in a.estados:
            erros.append(f"Transição ({origem}, {simbolo}): origem '{origem}' não pertence a Q")
        if simbolo not in a.alfabeto and simbolo != EPSILON:
            erros.append(f"Transição ({origem}, {simbolo}): símbolo '{simbolo}' não pertence a Σ ∪ {{ε}}")
        for destino in destinos:
            if destino not in a.estados:
                erros.append(f"Transição ({origem}, {simbolo}): destino '{destino}' não pertence a Q")

    return erros


def validar_palavra(a: Automato, palavra: str) -> list[str]:
    erros = []
    for simbolo in palavra:
        if simbolo not in a.alfabeto:
            erros.append(f"Palavra '{palavra}': símbolo '{simbolo}' não pertence ao alfabeto")
    return erros
