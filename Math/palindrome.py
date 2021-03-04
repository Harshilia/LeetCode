class Solution:
    def isPalindrome(self, x: int) -> bool:

        #Solution after converting integer to string
        # string = str(x)
        # if string != string[::-1]:return False
        # else:return True

        #Solution without converting integer to string
        if x < 0:
            return False
        temp, rev = x, 0
        while temp:
            rev = rev * 10 + temp % 10
            temp = int(temp/10)
        return rev == x
