from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # 1) Ordenar por end (criterio greedy: el que termina antes va primero)
        intervals.sort(key=lambda x: x[1])

        aceptados = 1                 # me quedo con el primero
        fin = intervals[0][1]         # end del último intervalo aceptado

        # 2) Una pasada: acepto el siguiente que no pisa al último aceptado
        for start, end in intervals[1:]:
            if start >= fin:          # no se solapa (tocarse está permitido)
                aceptados += 1
                fin = end
            # si start < fin, se solapa: este intervalo se "borra"

        # 3) Lo que no se aceptó es lo que se borra
        return len(intervals) - aceptados