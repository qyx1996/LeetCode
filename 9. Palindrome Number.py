class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return (0)
        elif x == 0:
            return (1)
        else:
            y = 0
            xx = x
            while xx != 0:
                a = xx % 10
                y = 10 * y + a
                xx = xx // 10
            if x == y:
                return (1)
            else:
                return (0)
