class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_s = {}
        for each in s:
            if each not in freq_s:
                freq_s[each] = 1
            else:
                freq_s[each] += 1

        for each in t:
            if each in freq_s:
                freq_s[each] -= 1
            else:
                return False

        for each in freq_s.values():
            if each != 0:
                return False

        return True
