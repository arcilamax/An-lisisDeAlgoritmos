from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        resultado = []
        actual = []                       # combinación que se va armando

        def backtrack(inicio, restante):
            if restante == 0:             # suma exacta: guardo una COPIA
                resultado.append(actual[:])
                return
            for i in range(inicio, len(candidates)):
                c = candidates[i]
                if c > restante:          # poda: se pasa, corto esta rama
                    continue
                actual.append(c)          # ELEGIR
                backtrack(i, restante - c)  # i (no i+1): se puede reutilizar
                actual.pop()              # DESHACER (backtrack)

        backtrack(0, target)
        return resultado