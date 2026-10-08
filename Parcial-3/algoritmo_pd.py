"""Algoritmo de Programación Dinámica: planificación de intervalos con peso.

ESTADO / SUBPROBLEMAS
    Con las reservas de un aula ordenadas por hora de fin (1..n):
    dp[i] = máximo ingreso usando solo las primeras i reservas.

RECURRENCIA
    p(i) = cantidad de reservas (en el orden) que terminan <= inicio de la reserva i,
           o sea, la última reserva compatible con i.

    dp[i] = max( dp[i-1],                    # no aceptar la reserva i
                 ingreso[i] + dp[p(i)] )     # aceptar la reserva i

CASO BASE
    dp[0] = 0  (sin reservas no hay ingreso)

COMPLEJIDAD
    O(n log n): ordenar + búsqueda binaria para p(i) + un recorrido de n.
"""
from bisect import bisect_right
from collections import defaultdict
from typing import Dict, List

from modelo import Reserva, Resultado


def ordenar_por_fin(reservas: List[Reserva]) -> List[Reserva]:
    return sorted(reservas, key=lambda r: (r.fin, r.inicio))


def calcular_p(ordenadas: List[Reserva]) -> List[int]:
    """p[i] (1-indexado) = cuántas reservas previas terminan <= inicio de la i."""
    n = len(ordenadas)
    fines = [r.fin for r in ordenadas]
    p = [0] * (n + 1)
    for i in range(1, n + 1):
        p[i] = bisect_right(fines, ordenadas[i - 1].inicio, 0, i - 1)
    return p


def llenar_tabla(ordenadas: List[Reserva], p: List[int]) -> List[int]:
    """Llena dp[0..n] aplicando la recurrencia."""
    n = len(ordenadas)
    dp = [0] * (n + 1)  # caso base: dp[0] = 0
    for i in range(1, n + 1):
        no_aceptar = dp[i - 1]
        aceptar = ordenadas[i - 1].ingreso + dp[p[i]]
        dp[i] = max(no_aceptar, aceptar)
    return dp


def reconstruir(ordenadas: List[Reserva], dp: List[int], p: List[int]) -> List[Reserva]:
    """Backtracking: recupera qué reservas conforman la solución óptima."""
    elegidas = []
    i = len(ordenadas)
    while i > 0:
        if dp[i] == dp[i - 1]:
            i -= 1                          # la reserva i no fue elegida
        else:
            elegidas.append(ordenadas[i - 1])
            i = p[i]                        # saltar a la última compatible
    elegidas.reverse()
    return elegidas


def planificar(reservas: List[Reserva]) -> Resultado:
    """Resuelve el problema para las reservas de UNA aula."""
    ordenadas = ordenar_por_fin(reservas)
    p = calcular_p(ordenadas)
    dp = llenar_tabla(ordenadas, p)
    elegidas = reconstruir(ordenadas, dp, p)
    return Resultado(dp[-1], elegidas, dp, p, ordenadas)


def planificar_por_aula(reservas: List[Reserva]) -> Dict[str, Resultado]:
    """Agrupa por aula y resuelve cada una de forma independiente."""
    por_aula = defaultdict(list)
    for r in reservas:
        por_aula[r.aula].append(r)
    return {aula: planificar(lista) for aula, lista in sorted(por_aula.items())}
