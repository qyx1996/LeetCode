def strReverse(strDemo):
    return strDemo[::-1]
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            y = str(-x)
            y = strReverse(y)
            z = - int(y)
            return (z if z > -2**31 else 0)
        elif x >= 0:
            y = str(x)
            y = strReverse(y)
            z = int(y)
            return (z if z < 2**31 else 0)
s = Solution()
print(s.reverse(-2147483646))