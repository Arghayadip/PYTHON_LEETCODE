import bisect
class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr2.sort()
        count = 0

        for x in arr1:
            left = 0
            right = len(arr2) - 1

            while left <= right:
                mid = (left + right) // 2

                if abs(x - arr2[mid]) <= d:
                    break
                elif arr2[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                count += 1

        return count