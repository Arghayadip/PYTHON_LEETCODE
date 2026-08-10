class Solution(object):
    def validMountainArray(self, nums):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n= len(nums)
        if n < 2:
            return False
        i = 0
        j = n-1
        while i<n-1 and nums[i]<nums[i+1]:
            i+=1
        while j>0 and nums[j]<nums[j-1]:
            j-=1
        return i == j and i!=0 and j!=n-1
            