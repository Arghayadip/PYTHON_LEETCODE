class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalindromeRange(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                # try skipping left char OR skipping right char
                return isPalindromeRange(i + 1, j) or isPalindromeRange(i, j - 1)
            i += 1
            j -= 1
        
        return True