
from entrada import carregar_automato
from nucleo import processar_palavra

a = carregar_automato("testes/cadeia_epsilon.json")

for palavra in a.palavras:

    passos, aceita = processar_palavra(a, palavra)

    print(f"\nPalavra: {palavra!r}")

    for simbolo, estados in passos:
        
        if simbolo is None:
            print("Inicial:", estados)
        else:
            print(f"Lido {simbolo!r}:", estados)

    print("ACEITA" if aceita else "REJEITADA")
