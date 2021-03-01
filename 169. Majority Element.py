class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]

    def majorityElement(self, nums): #Boyer-Moore Voting Algorithm
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate