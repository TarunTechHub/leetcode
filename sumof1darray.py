#Running Sum of 1d Array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        empty_array = [0] * len(nums)
        empty_array[0] = nums[0]
        for i in range(1,len(nums)):
            empty_array[i] = empty_array[i-1] + nums[i]
        return empty_array
