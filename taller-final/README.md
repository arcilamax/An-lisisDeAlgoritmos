# Taller final · Análisis de algoritmos · ITM 2026-2

Ocho problemas Medium de LeetCode, uno por familia. Lenguaje: **Python 3**.
Cada carpeta tiene `solution.py` (la clase `Solution` que se envió a LeetCode, con pruebas locales en `__main__`) y la captura del **Accepted** está en [`evidencias/`](evidencias/).

## Autoría

| Integrante | Usuario de git | Ejercicios |
| --- | --- | --- |
| Sara (arcilamax) | `arcilamax` | 215, 179 |
| María José Gallego | `MariaGallego23` | 72, 300 |
| Andrea Ramos | `Ann0806` | 134, 79 |
| Juan Robledo | `JuanRob2024` | 743, 1584 |

| # | Problema | Familia | Carpeta | Autor |
| --- | --- | --- | --- | --- |
| 1 | 215. Kth Largest Element in an Array | Heap | [kth-largest](kth-largest/) | `arcilamax` |
| 2 | 179. Largest Number | Ordenamiento (clave) | [largest-number](largest-number/) | `arcilamax` |
| 3 | 743. Network Delay Time | Grafos (Dijkstra) | [network-delay-time](network-delay-time/) | `JuanRob2024` |
| 4 | 1584. Min Cost to Connect All Points | Grafos (MST · Kruskal) | [min-cost-to-connect-all-points](min-cost-to-connect-all-points/) | `JuanRob2024` |
| 5 | 72. Edit Distance | Programación dinámica | [edit-distance](edit-distance/) | `MariaGallego23` |
| 6 | 300. Longest Increasing Subsequence | Programación dinámica | [longest-increasing-subsequence](longest-increasing-subsequence/) | `MariaGallego23` |
| 7 | 134. Gas Station | Greedy | [gas-station](gas-station/) | `Ann0806` |
| 8 | 79. Word Search | Backtracking | [word-search](word-search/) | `Ann0806` |

---

## 215. Kth Largest Element in an Array

Enlace: <https://leetcode.com/problems/kth-largest-element-in-an-array/>  
Autor: Sara (`arcilamax`)  
Código: [kth-largest/solution.py](kth-largest/solution.py)  
Familia: heap (el triaje)  
Idea: se mantiene un **min-heap de tamaño `k`** con los `k` mayores vistos. Si el heap está lleno y llega un valor mayor que la raíz, sale la raíz y entra el nuevo. Al terminar, la raíz es el k-ésimo mayor. No se ordena el arreglo completo.  
Complejidad: tiempo **`O(n log k)`** (cada uno de los `n` elementos hace a lo sumo una operación `O(log k)` en el heap); espacio extra **`O(k)`**. `n = len(nums)`.

## 179. Largest Number

Enlace: <https://leetcode.com/problems/largest-number/>  
Autor: Sara (`arcilamax`)  
Código: [largest-number/solution.py](largest-number/solution.py)  
Familia: ordenamiento (la clave)  
Idea: se pasan los números a cadena y se ordenan con el comparador **`a` antes que `b` si `a + b > b + a`** (concatenación, no suma). Así `2` va antes que `10` porque `"210" > "102"`. Si el resultado empieza en `"0"`, todo son ceros y se devuelve `"0"`.  
Complejidad: tiempo **`O(n log n)`** comparaciones, cada una `O(L)` (longitud de las cadenas, ≤ 10 dígitos); espacio **`O(n)`** para las cadenas y la salida. `n = len(nums)`.

## 743. Network Delay Time

Enlace: <https://leetcode.com/problems/network-delay-time/>  
Autor: Juan Robledo (`JuanRob2024`)  
Código: [network-delay-time/solution.py](network-delay-time/solution.py)  
Familia: grafos (Dijkstra)  
Modelo: grafo **dirigido y ponderado** (pesos ≥ 0); arco `u → v` con peso `w`, en lista de adyacencia.  
Idea: **Dijkstra desde `k`** con min-heap de distancia tentativa; se fija el nodo de menor tiempo acumulado y se relajan sus arcos. La respuesta es la **mayor** distancia final (hay que esperar al nodo que más tarda); si algún nodo no se alcanzó, `-1`.  
Complejidad: tiempo **`O((n + m) log n)`**, espacio **`O(n + m)`**. `n` = nodos, `m = len(times)`.

## 1584. Min Cost to Connect All Points

Enlace: <https://leetcode.com/problems/min-cost-to-connect-all-points/>  
Autor: Juan Robledo (`JuanRob2024`)  
Código: [min-cost-to-connect-all-points/solution.py](min-cost-to-connect-all-points/solution.py)  
Familia: grafos (árbol de recubrimiento mínimo) — **Kruskal**  
Modelo: grafo completo no dirigido; vértices = puntos, peso de cada arista = distancia de Manhattan.  
Idea: se generan las `n(n−1)/2` aristas, se **ordenan por peso** y se recorren: con **Union-Find** se acepta la arista si une componentes distintas y se rechaza si cerraría un ciclo. Se para al aceptar `n − 1` aristas; la suma de sus pesos es el costo.  
Complejidad: hay `Θ(n²)` aristas, así que el sort da tiempo **`O(n² log n)`** (Union-Find con compresión y rango es casi constante por operación); espacio **`O(n²)`** para la lista de aristas. `n = len(points`.

## 72. Edit Distance

Enlace: <https://leetcode.com/problems/edit-distance/>  
Autor: María José Gallego (`MariaGallego23`)  
Código: [edit-distance/solution.py](edit-distance/solution.py)  
Familia: programación dinámica (Wagner–Fischer)  
Estado: `dp[i][j]` = mínimo de ediciones para convertir `word1[0..i)` en `word2[0..j)`.  
Base: `dp[i][0] = i` (borrar `i` letras), `dp[0][j] = j` (insertar `j` letras).  
Recurrencia: si `word1[i−1] == word2[j−1]`, `dp[i][j] = dp[i−1][j−1]`; si no, `dp[i][j] = 1 + min(dp[i−1][j], dp[i][j−1], dp[i−1][j−1])` (borrar, insertar, sustituir). La respuesta es `dp[n][m]`.  
Complejidad: tiempo **`Θ(n·m)`**, espacio **`Θ(n·m)`**. `n = len(word1)`, `m = len(word2)`.

## 300. Longest Increasing Subsequence

Enlace: <https://leetcode.com/problems/longest-increasing-subsequence/>  
Autor: María José Gallego (`MariaGallego23`)  
Código: [longest-increasing-subsequence/solution.py](longest-increasing-subsequence/solution.py)  
Familia: programación dinámica  
Estado: `dp[i]` = longitud de la LIS estrictamente creciente que **termina** en el índice `i`.  
Base: `dp[i] = 1` (el elemento solo).  
Recurrencia: `dp[i] = max(dp[i], 1 + dp[j])` para todo `j < i` con `nums[j] < nums[i]`. La respuesta es `max(dp)`, no `dp[n−1]`.  
Complejidad: tiempo **`Θ(n²)`**, espacio **`Θ(n)`**. `n = len(nums)`.

## 134. Gas Station

Enlace: <https://leetcode.com/problems/gas-station/>  
Autor: Andrea Ramos (`Ann0806`)  
Código: [gas-station/solution.py](gas-station/solution.py)  
Familia: greedy  
Idea / criterio: una pasada sumando `gas[i] − cost[i]` a un tanque. Si el tanque queda **negativo** en `i`, se **descarta todo el tramo** desde el inicio candidato hasta `i`: cualquier estación intermedia llega a `i` con igual o menos combustible que el inicio (el prefijo que se salta tenía balance ≥ 0), así que tampoco pasa. El nuevo candidato es `i + 1` con tanque en 0 y no se vuelve atrás. Si `sum(gas) < sum(cost)` la respuesta es `-1`; si no, el último candidato es la salida (única).  
Complejidad: tiempo **`Θ(n)`**, espacio extra **`Θ(1)`**. `n = len(gas)`.

## 79. Word Search

Enlace: <https://leetcode.com/problems/word-search/>  
Autor: Andrea Ramos (`Ann0806`)  
Código: [word-search/solution.py](word-search/solution.py)  
Familia: backtracking  
Idea: desde cada celda se lanza `buscar(r, c, k)` (posición e índice de la letra que toca). **Se elige** un vecino ortogonal que coincida con `word[k]`, **se marca** la celda con `#` para no pisarla dos veces y se avanza a `k + 1`. Al volver, **se deshace** la marca (se restaura la letra) y se prueba otro vecino. La diagonal no es vecina.  
Complejidad: tiempo **`O(m·n·4^L)`** en el peor caso (cada arranque explora ramas de hasta 4 vecinos y profundidad `L`); espacio **`O(L)`** de la pila de recursión. Grilla `m × n`, `L = len(word)`.
