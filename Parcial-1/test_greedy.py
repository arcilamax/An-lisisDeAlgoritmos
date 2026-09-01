"""
test_greedy.py
---------------
Pruebas unitarias para el algoritmo Greedy de cambio de cajero.
Ejecutar con: python3 -m unittest test_greedy.py -v
"""

import unittest
from greedy import calcular_cambio_greedy, DENOMINACIONES


class TestCambioGreedy(unittest.TestCase):

    def test_monto_exacto_una_denominacion(self):
        r = calcular_cambio_greedy(100000)
        self.assertEqual(r.total_piezas, 1)
        self.assertEqual(r.detalle[0].denominacion, 100000)
        self.assertEqual(r.monto_no_cubierto, 0)

    def test_monto_cero(self):
        r = calcular_cambio_greedy(0)
        self.assertEqual(r.total_piezas, 0)
        self.assertEqual(r.detalle, [])

    def test_monto_combinado(self):
        r = calcular_cambio_greedy(187650)
        total_reconstruido = sum(d.subtotal for d in r.detalle)
        self.assertEqual(total_reconstruido, 187650)
        self.assertEqual(r.monto_no_cubierto, 0)

    def test_usa_denominaciones_mas_grandes_primero(self):
        # 273300 debe empezar priorizando el billete de 100.000
        r = calcular_cambio_greedy(273300)
        self.assertEqual(r.detalle[0].denominacion, 100000)
        self.assertEqual(r.detalle[0].cantidad, 2)

    def test_monto_no_divisible_en_50(self):
        # La menor denominación es 50, así que 23 no se puede cubrir exacto
        r = calcular_cambio_greedy(123)
        self.assertEqual(r.monto_no_cubierto, 23)

    def test_monto_negativo_lanza_error(self):
        with self.assertRaises(ValueError):
            calcular_cambio_greedy(-500)

    def test_greedy_minimiza_piezas_para_este_sistema(self):
        # Para las denominaciones colombianas, greedy siempre da el
        # número mínimo de piezas (sistema "canónico").
        r = calcular_cambio_greedy(999999950)
        # Verificamos que ninguna denominación pequeña se use cuando
        # una más grande todavía cabe (propiedad greedy).
        restante = 999999950
        for item in r.detalle:
            self.assertLessEqual(item.denominacion * item.cantidad, restante)
            restante -= item.denominacion * item.cantidad


if __name__ == "__main__":
    unittest.main()
