# Simulador de AFN-ε

Trabalho 01 de Teoria da Computação (UFPI). O programa lê um autômato finito com movimentos
vazios de um arquivo JSON e mostra, para cada palavra, os estados ativos a cada símbolo lido e
se ela foi aceita ou rejeitada.

## Requisitos

Python 3.10 ou mais novo. Não precisa instalar nada.

## Como executar

De dentro da pasta `simulador`:

```
python main.py testes/cadeia_epsilon.json
```

## Formato da entrada

```json
{
  "estados": ["q0", "q1", "q2"],
  "alfabeto": ["a", "b"],
  "inicial": "q0",
  "finais": ["q2"],
  "transicoes": [
    ["q0", "&", "q1"],
    ["q1", "a", "q1"],
    ["q1", "b", "q2"]
  ],
  "palavras": ["ab", "aab", "ba", ""]
}
```

Cada transição é `[origem, símbolo, destino]` e `&` representa ε. A palavra vazia é `""`.

## Testes

Os arquivos ficam em `simulador/testes/`:

- `sem_epsilon.json`: autômato sem transições ε
- `cadeia_epsilon.json`: cadeia de ε (q0 → q1 → q2)
- `ciclo_epsilon.json`: ciclo de ε (q0 → q1 → q0)
- `estado_morto.json`: a palavra "morre" no meio (ativos = ∅)
- `invalido.json`: erros propositais para testar a validação

Os resultados esperados estão em `simulador/resultados_esperados.md`. Cada parte também tem seu
teste separado: `testar_entrada.py`, `testar_nucleo.py` e `testar_saida.py`.
