# Resultados esperados dos testes

Calculados à mão (e conferidos). O simulador da Pessoa 2 deve produzir exatamente estes
conjuntos de estados ativos. Notação: `{...}` = estados ativos **depois** do fecho-ε; `∅` = conjunto vazio.

## sem_epsilon.json — palavras que terminam em "ab" (sem ε)

δ(q0,a) = {q0,q1}, δ(q0,b) = {q0}, δ(q1,b) = {q2}, F = {q2}

| Palavra | Início | Passos | Resultado |
|---|---|---|---|
| `ab`  | {q0} | a→{q0,q1}, b→{q0,q2} | ACEITA |
| `aab` | {q0} | a→{q0,q1}, a→{q0,q1}, b→{q0,q2} | ACEITA |
| `ba`  | {q0} | b→{q0}, a→{q0,q1} | REJEITADA |
| `""`  | {q0} | — | REJEITADA |
| `abb` | {q0} | a→{q0,q1}, b→{q0,q2}, b→{q0} | REJEITADA |
| `bab` | {q0} | b→{q0}, a→{q0,q1}, b→{q0,q2} | ACEITA |

## cadeia_epsilon.json — testa se o fecho-ε é transitivo (ε ∪ ab*)

δ(q0,ε) = {q1}, δ(q1,ε) = {q2}, δ(q2,a) = {q3}, δ(q3,b) = {q3}, F = {q2,q3}

Se o fecho-ε der só um passo, o início sai {q0,q1} (errado) e `""` e `a` passam a ser rejeitadas.

| Palavra | Início | Passos | Resultado |
|---|---|---|---|
| `""`  | {q0,q1,q2} | — | ACEITA |
| `a`   | {q0,q1,q2} | a→{q3} | ACEITA |
| `ab`  | {q0,q1,q2} | a→{q3}, b→{q3} | ACEITA |
| `abb` | {q0,q1,q2} | a→{q3}, b→{q3}, b→{q3} | ACEITA |
| `b`   | {q0,q1,q2} | b→∅ | REJEITADA |
| `aa`  | {q0,q1,q2} | a→{q3}, a→∅ | REJEITADA |

## ciclo_epsilon.json — testa se o fecho-ε trava em ciclo (a*b)

δ(q0,ε) = {q1}, δ(q1,ε) = {q0}, δ(q0,a) = {q0}, δ(q1,b) = {q2}, F = {q2}

Se o fecho-ε não usar conjunto de visitados, o programa entra em loop infinito já no início.

| Palavra | Início | Passos | Resultado |
|---|---|---|---|
| `b`   | {q0,q1} | b→{q2} | ACEITA |
| `ab`  | {q0,q1} | a→{q0,q1}, b→{q2} | ACEITA |
| `aab` | {q0,q1} | a→{q0,q1}, a→{q0,q1}, b→{q2} | ACEITA |
| `""`  | {q0,q1} | — | REJEITADA |
| `a`   | {q0,q1} | a→{q0,q1} | REJEITADA |
| `ba`  | {q0,q1} | b→{q2}, a→∅ | REJEITADA |

## estado_morto.json — testa o conjunto ativo virando ∅ (palavras que começam com "a")

δ(q0,a) = {q1}, δ(q1,a) = {q1}, δ(q1,b) = {q1}, F = {q1}  (não existe δ(q0,b))

| Palavra | Início | Passos | Resultado |
|---|---|---|---|
| `a`   | {q0} | a→{q1} | ACEITA |
| `ab`  | {q0} | a→{q1}, b→{q1} | ACEITA |
| `ba`  | {q0} | b→∅, a→∅ | REJEITADA |
| `bbb` | {q0} | b→∅, b→∅, b→∅ | REJEITADA |
| `""`  | {q0} | — | REJEITADA |

## invalido.json — testa as validações de entrada

Deve gerar **7 erros** no autômato e **1 erro** de palavra:

1. Estado inicial `q9` não pertence a Q
2. Estado final `q5` não pertence a Q
3. `&` (ε) não pode pertencer ao alfabeto
4. Símbolo `bc` do alfabeto tem mais de 1 caractere
5. Transição (q7, a): origem `q7` não pertence a Q
6. Transição (q0, x): símbolo `x` não pertence a Σ ∪ {ε}
7. Transição (q1, &): destino `q8` não pertence a Q

Palavras: `aa` válida; `az` inválida (`z` ∉ Σ).

A transição (q0, a) → q1 é válida de propósito, para conferir que a validação não gera alarme falso.
