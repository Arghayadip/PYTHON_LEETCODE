class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) < len(needle):
            return -1
        i = 0
        count = 0
        while i<=len(haystack) - len(needle):
            j =0
            while j<len(needle):
                if haystack[i+j] == needle[j]:
                    j += 1
                else:
                    break
            if j == len(needle):
                return i
            i+=1
        return -1
