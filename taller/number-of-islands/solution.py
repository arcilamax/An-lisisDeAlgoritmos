from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        islas = 0
        direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # sin diagonales

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':          # tierra no visitada
                    islas += 1                 # nueva componente conexa
                    grid[i][j] = '0'           # la marco como visitada ("hundo")
                    pila = [(i, j)]

                    while pila:                # DFS: hundo toda la isla
                        x, y = pila.pop()
                        for dx, dy in direcciones:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                                grid[nx][ny] = '0'
                                pila.append((nx, ny))
        return islas