
from saida import formatar_conjunto, exibir_computacao

print(formatar_conjunto({"q2", "q0", "q1"}))
print(formatar_conjunto(set()))

print()
exibir_computacao("ab", [(None, {"q0", "q1"}), ("a", {"q1"}), ("b", {"q2"})], True, {"q2"})

print()
exibir_computacao("ba", [(None, {"q0", "q1"}), ("b", set()), ("a", set())], False, {"q2"})

print()
exibir_computacao("", [(None, {"q0", "q1", "q2"})], True, {"q2"})
