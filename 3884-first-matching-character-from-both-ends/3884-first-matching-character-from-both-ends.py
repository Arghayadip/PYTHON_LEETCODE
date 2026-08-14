class Solution(object):
    def firstMatchingIndex(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        for i in range(0,n//2+1):
            if s[i] == s[n-i-1]:
                return i
            i+= 1
        return -1
        