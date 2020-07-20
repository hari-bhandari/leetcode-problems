from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        for i, num in enumerate(nums):
            sum += num
            nums[i] = sum
        return nums