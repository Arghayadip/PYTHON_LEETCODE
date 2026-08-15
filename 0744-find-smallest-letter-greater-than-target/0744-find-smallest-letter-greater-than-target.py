class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        n = len(letters)
        l = 0
        h = n-1
        while l <= h:
            mid = (l+h)//2
            if letters[mid] > target:
                h = mid -1
            else:
                l = mid + 1
        return letters[l % n]
