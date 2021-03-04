class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        freq_ransomNote = collections.Counter(ransomNote)
        freq_magazine = collections.Counter(magazine)

        # for key,value in freq_ransomNote.items():
        #     if key not in freq_magazine.keys():
        #         return False
        #     if value>freq_magazine[key]:
        #         return False
        # return True

        # Efficient solution
        return not(freq_ransomNote - freq_magazine)
