from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1) Ordenar los intervalos por extremo izquierdo (start)
        intervals = self._merge_sort(intervals)

        # 2) Una pasada: fusionar lo que se solapa o se toca
        result = [intervals[0][:]]          # intervalo "abierto" actual
        for start, end in intervals[1:]:
            last = result[-1]
            if start <= last[1]:            # se solapa o se toca
                last[1] = max(last[1], end) # ensancho el end
            else:                           # no se solapa
                result.append([start, end]) # cierro el actual y abro otro
        return result

    # ---------- Merge sort sobre intervalos, clave = start ----------
    def _merge_sort(self, arr: List[List[int]]) -> List[List[int]]:
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self._merge_sort(arr[:mid])
        right = self._merge_sort(arr[mid:])
        return self._combine(left, right)

    def _combine(self, left: List[List[int]], right: List[List[int]]) -> List[List[int]]:
        out = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                out.append(left[i])
                i += 1
            else:
                out.append(right[j])
                j += 1
        out.extend(left[i:])
        out.extend(right[j:])
        return out