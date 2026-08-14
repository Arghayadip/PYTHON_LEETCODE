class Solution(object):
    def reverseByType(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        s = list(s)
        i = 0
        j = n-1
        while i< j:
            if not s[i].isalpha():
                i+=1
            elif not s[j].isalpha():
                j-=1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        i = 0
        j = n-1
        while i< j:
            if s[i].isalpha():
                i+=1
            elif s[j].isalpha():
                j-=1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(s)
