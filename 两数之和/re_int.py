#整数反转
class Solution:
    def reverse(self, x: int) -> int:
            if x == 0:
                c = 0
            elif x < 0:
                x = -x
                c = int(''.join([x for x in str(x)][::-1]))
                c = -c
            else:
                c = int(''.join([x for x in str(x)][::-1]))
            if pow(-2, 31) > c or c > pow(2, 31)-1:
                return 0
            else:
                return c
