class Solution(object):
    def minimumSwaps(self, nums):
        swap = 0
        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[i] == 0:
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    swap += 1
                    i += 1
                j -= 1
            else:
                i += 1

        return swap