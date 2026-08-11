class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        closest_sum=nums[0]+nums[1]+nums[2]
        for i in range(0,n-2):
            j=i+1
            k=n-1
            while j<k:
                total= nums[i]+nums[j]+nums[k]

                if abs(total - target) < abs(closest_sum - target):
                    closest_sum= total
                if total == target:
                     return target
                elif total < target:
                    j+=1
                else: 
                    k-=1
        return closest_sum
                