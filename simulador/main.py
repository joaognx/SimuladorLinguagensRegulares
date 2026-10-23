import sys
from entrada import carregar_automato
from validacao import validar_automato, validar_palavra
from nucleo import processar_palavra
from saida import exibir_computacao


def main():

    if len(sys.argv) != 2:
        print("Uso: python main.py <arquivo.json>")
        return

    try:
        a = carregar_automato(sys.argv[1])
    except Exception as e:
        print("Erro ao ler o arquivo:", e)
        return

    erros = validar_automato(a)
    if erros:
        print("Autômato inválido:")
        for erro in erros:
            print("  -", erro)
        return

    for palavra in a.palavras:

        print("-" * 40)

        erros_palavra = validar_palavra(a, palavra)
        if erros_palavra:
            print(f'Palavra: "{palavra}"')
            print(erros_palavra[0])
            print("REJEITADA")
            continue

        passos, aceita = processar_palavra(a, palavra)
        exibir_computacao(palavra, passos, aceita, a.finais)


main()
