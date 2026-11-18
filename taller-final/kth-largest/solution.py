# 215. Kth Largest Element in an Array
# Familia: heap (triaje). Min-heap de tamaño k: la raíz es el k-ésimo mayor.
# Tiempo O(n log k), espacio extra O(k). n = len(nums).
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap: List[int] = []  # min-heap con a lo sumo k elementos
        for x in nums:
            if len(heap) < k:
                heapq.heappush(heap, x)
            elif x > heap[0]:
                # x supera al menor de los k mejores: sale la raíz, entra x
                heapq.heapreplace(heap, x)
        return heap[0]


if __name__ == "__main__":
    s = Solution()
    assert s.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert s.findKthLargest([1], 1) == 1
    print("215 OK")
