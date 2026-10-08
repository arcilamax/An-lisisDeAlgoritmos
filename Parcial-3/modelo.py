"""Modelos de datos del sistema de reservas de aulas."""
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Reserva:
    """Solicitud de reserva de un aula.

    inicio y fin son horas en formato 24h (enteros). El intervalo es [inicio, fin):
    una reserva que termina a las 10 es compatible con otra que empieza a las 10.
    """
    aula: str
    solicitante: str
    inicio: int
    fin: int
    ingreso: int  # valor de la reserva en pesos COP

    def __post_init__(self):
        if self.fin <= self.inicio:
            raise ValueError(f"Horario inválido en '{self.solicitante}': fin <= inicio")
        if self.ingreso < 0:
            raise ValueError(f"Ingreso negativo en '{self.solicitante}'")

    def se_cruza_con(self, otra: "Reserva") -> bool:
        return self.inicio < otra.fin and otra.inicio < self.fin


@dataclass
class Resultado:
    """Resultado de planificar las reservas de UNA aula."""
    maximo: int                  # ingreso máximo
    elegidas: List[Reserva]      # reservas aceptadas
    dp: List[int]                # tabla de PD: dp[i]
    p: List[int]                 # p[i]: última reserva compatible con i
    ordenadas: List[Reserva]     # reservas ordenadas por hora de fin
