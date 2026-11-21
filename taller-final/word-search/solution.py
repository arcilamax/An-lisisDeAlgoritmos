# 79. Word Search
# Familia: backtracking. Se ELIGE una celda vecina (arriba/abajo/izq/der) que
# coincide con la siguiente letra, se MARCA y se avanza; si la rama no completa la
# palabra se DESHACE la marca (se restaura la letra) y se prueba otro vecino.
# Tiempo O(m·n·4^L) en el peor caso, espacio O(L) de la pila de recursión.
# m × n = tamaño de la grilla, L = len(word).
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        filas, cols = len(board), len(board[0])

        def buscar(r: int, c: int, k: int) -> bool:
            # k = índice de la letra de word que toca en (r, c)
            if k == len(word):
                return True
            if r < 0 or r >= filas or c < 0 or c >= cols or board[r][c] != word[k]:
                return False

            letra = board[r][c]
            board[r][c] = "#"  # elegir: marcar la celda como usada
            encontrado = (
                buscar(r + 1, c, k + 1)
                or buscar(r - 1, c, k + 1)
                or buscar(r, c + 1, k + 1)
                or buscar(r, c - 1, k + 1)
            )
            board[r][c] = letra  # deshacer: quitar la marca
            return encontrado

        for r in range(filas):
            for c in range(cols):
                if buscar(r, c, 0):
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    tablero = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert s.exist([fila[:] for fila in tablero], "ABCCED") is True
    assert s.exist([fila[:] for fila in tablero], "SEE") is True
    assert s.exist([fila[:] for fila in tablero], "ABCB") is False
    print("79 OK")
