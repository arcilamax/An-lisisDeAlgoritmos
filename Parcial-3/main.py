"""Punto de entrada: reserva de aulas maximizando ingresos con Programación Dinámica.

Uso:
    python main.py                 # todas las aulas, con tablas de PD
    python main.py --aula "Aula 101"
    python main.py --sin-tabla
"""
import argparse

from algoritmo_pd import planificar_por_aula
from datos import solicitudes_ejemplo
from reportes import imprimir_resultado, imprimir_tabla
from voraz import voraz_por_ingreso


def main():
    parser = argparse.ArgumentParser(description="Reserva óptima de aulas (PD)")
    parser.add_argument("--aula", help="Procesar solo esta aula")
    parser.add_argument("--sin-tabla", action="store_true", help="No imprimir la tabla de PD")
    args = parser.parse_args()

    solicitudes = solicitudes_ejemplo()
    if args.aula:
        solicitudes = [r for r in solicitudes if r.aula == args.aula]
        if not solicitudes:
            print(f"No hay solicitudes para el aula '{args.aula}'.")
            return

    resultados = planificar_por_aula(solicitudes)
    total_pd = total_voraz = 0

    for aula, res in resultados.items():
        print("=" * 74)
        print(f"{aula.upper()}  ({len(res.ordenadas)} solicitudes)")
        print("=" * 74)
        if not args.sin_tabla:
            imprimir_tabla(res)
        voraz_total, _ = voraz_por_ingreso(res.ordenadas)
        imprimir_resultado(aula, res, voraz_total)
        total_pd += res.maximo
        total_voraz += voraz_total

    print("\n" + "=" * 74)
    print("RESUMEN GENERAL")
    print("=" * 74)
    print(f"Ingreso total con PD:     ${total_pd:,} COP")
    print(f"Ingreso total con voraz:  ${total_voraz:,} COP")
    print(f"Ganancia total por PD:    ${total_pd - total_voraz:,} COP")


if __name__ == "__main__":
    main()
