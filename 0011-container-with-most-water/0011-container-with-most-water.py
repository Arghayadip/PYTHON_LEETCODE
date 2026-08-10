class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        maxi = 0
        i=0
        j=n-1
        while i<j:
            contain = min(height[i],height[j])*(j-i)
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
            maxi = max(maxi,contain)
        return maxi
        


