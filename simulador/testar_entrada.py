from pathlib import Path
from entrada import carregar_automato
from validacao import validar_automato, validar_palavra

PASTA_TESTES = Path(__file__).parent / "testes"

for arquivo in sorted(PASTA_TESTES.glob("*.json")):
    print("=" * 60)
    print("Arquivo:", arquivo.name)
    a = carregar_automato(arquivo)

    erros = validar_automato(a)
    if erros:
        print(f"Autômato INVÁLIDO ({len(erros)} erro(s)):")
        for erro in erros:
            print("  -", erro)
    else:
        print("Autômato válido.")

    for p in a.palavras:
        erros_palavra = validar_palavra(a, p)
        situacao = "ok" if not erros_palavra else "; ".join(erros_palavra)
        print(f"  palavra {p!r}: {situacao}")
