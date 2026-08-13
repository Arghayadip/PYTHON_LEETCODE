class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        while not all(nums[i]<=nums[i+1] for i in range(0,len(nums)-1)):
            mini = float("inf")
            mini_index = 0
            for i in range(0,len(nums)-1):
                total = nums[i]+nums[i+1]

                if total < mini:
                    mini = total
                    min_index = i
            nums[min_index] = mini
            nums.pop(min_index + 1)

            count += 1
        return count


        
