"""Estrategia voraz de comparación: aceptar siempre la reserva más cara que no se cruce.

Sirve para demostrar que una heurística simple NO siempre es óptima y que la
Programación Dinámica sí lo es.
"""
from typing import List, Tuple

from modelo import Reserva


def voraz_por_ingreso(reservas: List[Reserva]) -> Tuple[int, List[Reserva]]:
    aceptadas: List[Reserva] = []
    for r in sorted(reservas, key=lambda x: -x.ingreso):
        if all(not r.se_cruza_con(a) for a in aceptadas):
            aceptadas.append(r)
    aceptadas.sort(key=lambda x: x.inicio)
    return sum(r.ingreso for r in aceptadas), aceptadas
