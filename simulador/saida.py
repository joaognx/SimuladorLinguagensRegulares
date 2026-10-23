def formatar_conjunto(estados: set[str]) -> str:

    if not estados:
        return "∅"

    return "{" + ", ".join(sorted(estados)) + "}"


def exibir_computacao(palavra, passos, aceita, finais):

    print(f'Palavra: "{palavra}"')

    for simbolo, estados in passos:

        if simbolo is None:
            print("Estados iniciais (fecho-ε):", formatar_conjunto(estados))
        else:
            print(f"Lido '{simbolo}' ->", formatar_conjunto(estados))

    ativos = passos[-1][1]

    if aceita:
        print(f"Ativos ∩ F = {formatar_conjunto(ativos & finais)} ≠ ∅  =>  ACEITA")
    else:
        print("Ativos ∩ F = ∅  =>  REJEITADA")
