class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        left, right = 0, nums[0]
        times = 1
        while right < len(nums) - 1:
            times += 1
            left, right = right, max(i + nums[i] for i in range(left, right + 1))
        return times
