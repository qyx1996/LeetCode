class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        max = nums[0]
        min = nums[-1]
        start = 0
        end = -1
        for i in range(len(nums)):
            if nums[i] < max:
                end = i
            else:
                max = nums[i]
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > min:
                start = i
            else:
                min = nums[i]
        return end - start + 1