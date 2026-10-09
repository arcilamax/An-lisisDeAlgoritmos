"""Pruebas del algoritmo. Ejecutar con:  python -m unittest -v"""
import random
import unittest
from itertools import combinations

from algoritmo_pd import planificar, planificar_por_aula
from datos import solicitudes_ejemplo
from modelo import Reserva
from voraz import voraz_por_ingreso


def R(inicio, fin, ingreso, aula="A", nombre="x"):
    return Reserva(aula, nombre, inicio, fin, ingreso)


def fuerza_bruta(reservas):
    """Prueba todos los subconjuntos válidos (solo para n pequeño)."""
    mejor = 0
    for k in range(len(reservas) + 1):
        for sub in combinations(reservas, k):
            if all(not a.se_cruza_con(b) for a, b in combinations(sub, 2)):
                mejor = max(mejor, sum(r.ingreso for r in sub))
    return mejor


class TestCasosBase(unittest.TestCase):
    def test_sin_reservas(self):
        res = planificar([])
        self.assertEqual(res.maximo, 0)
        self.assertEqual(res.elegidas, [])

    def test_una_reserva(self):
        res = planificar([R(8, 10, 100)])
        self.assertEqual(res.maximo, 100)
        self.assertEqual(len(res.elegidas), 1)


class TestCasosPequenos(unittest.TestCase):
    def test_sin_cruces_se_aceptan_todas(self):
        res = planificar([R(8, 9, 10), R(9, 10, 20), R(10, 11, 30)])
        self.assertEqual(res.maximo, 60)

    def test_borde_fin_igual_a_inicio_es_compatible(self):
        res = planificar([R(8, 10, 50), R(10, 12, 70)])
        self.assertEqual(res.maximo, 120)

    def test_cruce_total_elige_la_mas_cara(self):
        res = planificar([R(8, 12, 10), R(9, 11, 99), R(10, 13, 40)])
        self.assertEqual(res.maximo, 99)

    def test_pd_supera_al_voraz(self):
        # La más cara (100) bloquea dos que suman 160
        reservas = [R(0, 10, 100), R(0, 5, 80), R(5, 10, 80)]
        self.assertEqual(planificar(reservas).maximo, 160)
        self.assertEqual(voraz_por_ingreso(reservas)[0], 100)

    def test_solucion_reconstruida_es_valida_y_suma_el_maximo(self):
        res = planificar(solicitudes_ejemplo()[:10])
        for a, b in combinations(res.elegidas, 2):
            self.assertFalse(a.se_cruza_con(b))
        self.assertEqual(sum(r.ingreso for r in res.elegidas), res.maximo)


class TestContraFuerzaBruta(unittest.TestCase):
    def test_aleatorios(self):
        rng = random.Random(42)
        for _ in range(300):
            n = rng.randint(0, 9)
            reservas = []
            for _ in range(n):
                ini = rng.randint(0, 12)
                reservas.append(R(ini, ini + rng.randint(1, 5), rng.randint(0, 500)))
            self.assertEqual(planificar(reservas).maximo, fuerza_bruta(reservas))


class TestPorAula(unittest.TestCase):
    def test_cada_aula_es_independiente(self):
        # Mismo horario en aulas distintas NO es conflicto
        reservas = [R(8, 10, 100, aula="A"), R(8, 10, 200, aula="B")]
        res = planificar_por_aula(reservas)
        self.assertEqual(res["A"].maximo, 100)
        self.assertEqual(res["B"].maximo, 200)

    def test_datos_de_ejemplo(self):
        res = planificar_por_aula(solicitudes_ejemplo())
        self.assertEqual(set(res), {"Aula 101", "Aula 202", "Auditorio"})
        self.assertEqual(res["Aula 101"].maximo, 930_000)


if __name__ == "__main__":
    unittest.main()
