class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if trust:
            judge = [0]*(N+1)
            for a,b in trust:
                judge[a] -= 1
                judge[b] += 1
            for i,each in enumerate(judge):
                if each == N-1:
                    return i
            return -1
        else:
            return 1