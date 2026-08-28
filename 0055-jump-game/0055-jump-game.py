class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_idx = 0
        n = len(nums)
        for i in range( 0, n ):
            if i>max_idx:
                return False
            max_idx = max(max_idx, i+nums[i])
        return True 
