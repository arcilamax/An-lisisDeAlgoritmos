# 179. Largest Number
# Familia: ordenamiento (la clave). a va antes que b si a+b > b+a (concatenación).
# Tiempo O(n log n) comparaciones, cada una O(L) con L = longitud de las cadenas.
# Espacio O(n) para las cadenas y la salida. n = len(nums).
from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = [str(x) for x in nums]

        def comparar(a: str, b: str) -> int:
            if a + b > b + a:
                return -1  # a primero
            if a + b < b + a:
                return 1   # b primero
            return 0

        strs.sort(key=cmp_to_key(comparar))
        resultado = "".join(strs)
        # Si el primero es "0", todos son ceros: "00" -> "0"
        return "0" if resultado[0] == "0" else resultado


if __name__ == "__main__":
    s = Solution()
    assert s.largestNumber([10, 2]) == "210"
    assert s.largestNumber([3, 30, 34, 5, 9]) == "9534330"
    assert s.largestNumber([0, 0]) == "0"
    print("179 OK")
