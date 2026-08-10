class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        result = [0]*n
        i=0
        j=n-1
        pos = n-1
        while i<=j:
            left_sq = nums[i]*nums[i]
            right_sq = nums[j]*nums[j]

            if left_sq > right_sq:
                result[pos]= left_sq
                i+=1
            else:
                result[pos]=right_sq
                j-=1
            pos-=1
        return result
            

