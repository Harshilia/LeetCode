class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        len_text1 = len(text1)
        len_text2 = len(text2)
        dp_array = [[0]*(len_text2+1) for i in range(len_text1+1)]

        for i in range(len_text1+1):
            for j in range(len_text2+1):
                if i==0 or j==0:
                    dp_array[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    dp_array[i][j] = dp_array[i-1][j-1] + 1
                else:
                    dp_array[i][j] = max(dp_array[i-1][j], dp_array[i][j-1])
        return dp_array[len_text1][len_text2]
