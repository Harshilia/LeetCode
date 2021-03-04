class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in "!?',;.": paragraph = paragraph.replace(c, " ")
        paragraph = paragraph.lower().split()
        return collections.Counter(each for each in paragraph if each not in banned).most_common()[0][0]