# 300. Longest Increasing Subsequence
# Familia: programación dinámica (versión de pizarrón Θ(n²)).
# Estado: dp[i] = longitud de la LIS que TERMINA en el índice i.
# Base: dp[i] = 1 (el elemento solo).
# Recurrencia: dp[i] = max(dp[i], 1 + dp[j]) para todo j < i con nums[j] < nums[i].
# Respuesta: max(dp) (la LIS puede no terminar en el último).
# Tiempo Θ(n²), espacio Θ(n). n = len(nums).
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)


if __name__ == "__main__":
    s = Solution()
    assert s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert s.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    assert s.lengthOfLIS([7, 7, 7, 7]) == 1
    print("300 OK")
