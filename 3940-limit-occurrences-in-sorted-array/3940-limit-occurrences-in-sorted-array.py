class Solution(object):
    def limitOccurrences(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        j = 0
        for i in range (0,len(nums)):
            if j<k or nums[i] != nums[j-k]:
                nums[j] = nums[i]
                j += 1
        return nums[:j]