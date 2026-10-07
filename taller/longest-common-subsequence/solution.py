from typing import List

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)

        # dp[i][j] = LCS de text1[0..i) y text2[0..j)
        # La fila 0 y la columna 0 quedan en 0 (prefijo vacío)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]       # coinciden: extiendo
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # no coinciden: mejor de los dos
        return dp[n][m]