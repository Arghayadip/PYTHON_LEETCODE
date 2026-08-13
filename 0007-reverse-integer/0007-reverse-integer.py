class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        total = 0
        while x != 0:
            digit = x % 10
            total = total * 10 + digit
            x = x//10
        result = total*sign
        
        if result < -(2**31) or result > 2**31-1:
            return 0
        else:
            return result


