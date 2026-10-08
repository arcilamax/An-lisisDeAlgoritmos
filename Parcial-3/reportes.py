"""Impresión de tablas y resultados en consola."""
from modelo import Resultado


def imprimir_tabla(res: Resultado) -> None:
    print(f"{'i':>2} | {'Solicitante':<26} | {'Horario':<9} | {'Ingreso':>9} | {'p(i)':>4} | {'dp[i]':>9}")
    print("-" * 74)
    print(f"{0:>2} | {'(caso base)':<26} | {'-':<9} | {'-':>9} | {'-':>4} | {res.dp[0]:>9,}")
    for i, r in enumerate(res.ordenadas, start=1):
        horario = f"{r.inicio}-{r.fin}h"
        print(f"{i:>2} | {r.solicitante:<26} | {horario:<9} | {r.ingreso:>9,} | {res.p[i]:>4} | {res.dp[i]:>9,}")


def imprimir_resultado(aula: str, res: Resultado, voraz_total: int) -> None:
    print(f"\nReservas aceptadas en {aula}:")
    for r in res.elegidas:
        print(f"  - {r.solicitante:<26} {r.inicio}-{r.fin}h  ${r.ingreso:,}")
    print(f"Ingreso máximo (PD):          ${res.maximo:,} COP")
    print(f"Estrategia voraz (más cara):  ${voraz_total:,} COP")
    print(f"Ganancia de usar PD:          ${res.maximo - voraz_total:,} COP")
