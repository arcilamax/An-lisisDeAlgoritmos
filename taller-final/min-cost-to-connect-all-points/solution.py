# 1584. Min Cost to Connect All Points
# Familia: grafos (árbol de recubrimiento mínimo) — KRUSKAL con Union-Find.
# Modelo: grafo completo no dirigido; vértices = puntos, peso = distancia Manhattan.
# Se ordenan las Θ(n²) aristas por peso y se toma cada una si une componentes
# distintas (si cerraría un ciclo, se rechaza). Se para al tener n - 1 aristas.
# Tiempo O(n² log n) por el sort, espacio O(n²) para la lista de aristas.
# n = len(points).
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        aristas = []
        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                aristas.append((abs(xi - xj) + abs(yi - yj), i, j))
        aristas.sort()

        padre = list(range(n))
        rango = [0] * n

        def find(x: int) -> int:
            while padre[x] != x:
                padre[x] = padre[padre[x]]  # compresión de camino
                x = padre[x]
            return x

        def union(a: int, b: int) -> bool:
            ra, rb = find(a), find(b)
            if ra == rb:
                return False  # cerraría un ciclo
            if rango[ra] < rango[rb]:
                ra, rb = rb, ra
            padre[rb] = ra
            if rango[ra] == rango[rb]:
                rango[ra] += 1
            return True

        costo, usadas = 0, 0
        for w, i, j in aristas:
            if union(i, j):
                costo += w
                usadas += 1
                if usadas == n - 1:
                    break
        return costo


if __name__ == "__main__":
    s = Solution()
    assert s.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20
    assert s.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]) == 18
    assert s.minCostConnectPoints([[0, 0]]) == 0
    print("1584 OK")
