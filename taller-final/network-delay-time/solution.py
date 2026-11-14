# 743. Network Delay Time
# Familia: grafos (Dijkstra). Modelo: grafo DIRIGIDO y PONDERADO (pesos >= 0),
# arco u -> v con peso w. Dijkstra desde k con min-heap de distancia tentativa.
# Respuesta: la MAYOR distancia finita (hay que esperar al nodo que más tarda);
# si algún nodo queda inalcanzable, -1.
# Tiempo O((n + m) log n), espacio O(n + m). n = nodos, m = len(times).
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        grafo = defaultdict(list)  # lista de adyacencia: u -> [(v, w)]
        for u, v, w in times:
            grafo[u].append((v, w))

        dist = {}             # distancias definitivas
        heap = [(0, k)]       # (distancia tentativa, nodo)
        while heap:
            d, u = heapq.heappop(heap)
            if u in dist:
                continue      # ya se fijó con una distancia menor
            dist[u] = d
            for v, w in grafo[u]:
                if v not in dist:
                    heapq.heappush(heap, (d + w, v))

        if len(dist) < n:
            return -1
        return max(dist.values())


if __name__ == "__main__":
    s = Solution()
    assert s.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
    assert s.networkDelayTime([[1, 2, 1]], 2, 1) == 1
    assert s.networkDelayTime([[1, 2, 1]], 2, 2) == -1
    print("743 OK")
