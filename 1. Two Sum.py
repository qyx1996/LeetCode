class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            minus = target - num
            if minus in nums[i+1:]:
                j = nums[i+1:].index(minus) + i + 1
                return [i, j]