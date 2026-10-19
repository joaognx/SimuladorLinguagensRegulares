from dataclasses import dataclass, field

EPSILON = "&"

@dataclass
class Automato:
    estados: set[str]
    alfabeto: set[str]
    inicial: str
    finais: set[str]
    transicoes: dict[tuple[str, str], set[str]]
    palavras: list[str] = field(default_factory=list)
