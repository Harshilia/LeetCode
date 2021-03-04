class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit = []
        letter = []
        for each in logs:
            if each.split()[1].isdigit():
                digit.append(each)
            else:
                letter.append(each)
        letter.sort(key=lambda log: log.split()[0])
        letter.sort(key=lambda log: log.split()[1:])

        return letter + digit