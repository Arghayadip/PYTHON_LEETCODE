class Solution(object):
    def minimumSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        swap = 0
        n = len(nums)
        i = 0
        j = n-1
        while i<j:
            if nums[i] == 0 and nums[j] != 0:
                nums[i],nums[j] = nums[j], nums[i]
                swap += 1
                i += 1
                j -= 1
            elif nums[i] == 0 and nums[j]== 0:
                j -= 1
            elif nums[i] != 0 and nums[j]== 0:
                j -= 1
            elif nums[i] != 0 and nums[j] != 0:
                i+=1
        return swap
