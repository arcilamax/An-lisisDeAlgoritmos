"""
greedy.py
---------
Algoritmo Greedy (voraz) para calcular el cambio óptimo que debe
entregar un cajero automático, usando el menor número posible de
billetes y monedas.

Idea del algoritmo:
En cada paso se elige la denominación más grande que sea menor o
igual al monto restante, y se usa tantas veces como sea posible
antes de pasar a la siguiente denominación más pequeña. Esta
decisión "voraz" (tomar lo mejor disponible en el momento, sin
mirar atrás) es óptima para el sistema de denominaciones colombiano,
porque cada denominación es múltiplo -o casi múltiplo- de la
siguiente, lo que evita casos en los que la elección local no
lleve al óptimo global.
"""

from dataclasses import dataclass, field

# Denominaciones disponibles en un cajero colombiano, de mayor a menor.
DENOMINACIONES = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50]


@dataclass
class DetalleDenominacion:
    denominacion: int
    cantidad: int
    subtotal: int

@dataclass
class ResultadoCambio:
    monto_solicitado: int
    detalle: list = field(default_factory=list)
    total_piezas: int = 0
    monto_no_cubierto: int = 0

    def to_dict(self):
        return {
            "monto_solicitado": self.monto_solicitado,
            "detalle": [
                {
                    "denominacion": d.denominacion,
                    "cantidad": d.cantidad,
                    "subtotal": d.subtotal,
                }
                for d in self.detalle
            ],
            "total_piezas": self.total_piezas,
            "monto_no_cubierto": self.monto_no_cubierto,
        }


def calcular_cambio_greedy(monto, denominaciones=None):
    """
    Calcula la combinación de billetes/monedas que entrega el cajero
    usando la estrategia Greedy: en cada paso toma la denominación más
    grande disponible que quepa en el monto restante.

    Parámetros
    ----------
    monto : int
        Monto total a entregar, en pesos colombianos (COP).
    denominaciones : list[int], opcional
        Lista de denominaciones a usar, de mayor a menor.
        Por defecto usa DENOMINACIONES.

    Retorna
    -------
    ResultadoCambio
        Objeto con el detalle de billetes/monedas entregados, el total
        de piezas usadas y el monto que no se pudo cubrir (si la
        denominación más pequeña no permite completar el monto exacto).
    """
    if monto < 0:
        raise ValueError("El monto no puede ser negativo.")

    denominaciones = denominaciones or DENOMINACIONES
    denominaciones = sorted(denominaciones, reverse=True)

    restante = int(monto)
    detalle = []

    for d in denominaciones:
        if restante <= 0:
            break
        cantidad = restante // d
        if cantidad > 0:
            detalle.append(DetalleDenominacion(d, cantidad, cantidad * d))
            restante -= cantidad * d

    total_piezas = sum(item.cantidad for item in detalle)

    return ResultadoCambio(
        monto_solicitado=int(monto),
        detalle=detalle,
        total_piezas=total_piezas,
        monto_no_cubierto=restante,
    )


if __name__ == "__main__":
    # Prueba rápida por consola
    for prueba in [187650, 100000, 50, 273300, 0]:
        r = calcular_cambio_greedy(prueba)
        print(f"\nMonto solicitado: ${prueba:,}")
        for item in r.detalle:
            print(f"  {item.cantidad} x ${item.denominacion:,} = ${item.subtotal:,}")
        print(f"  Total de piezas entregadas: {r.total_piezas}")
        if r.monto_no_cubierto:
            print(f"  ⚠ Monto no cubierto (no divisible en $50): ${r.monto_no_cubierto}")
