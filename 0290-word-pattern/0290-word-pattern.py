class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(pattern) != len(words):
            return False
        map_p = {}
        map_w = {}
        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]

            if p in map_p and map_p[p] != w:
                return False
            if w in map_w and map_w[w] != p:
                return False
            map_p[p] = w
            map_w[w] = p
        return True