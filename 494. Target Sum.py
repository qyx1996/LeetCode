# recursion (Brute Force)
class Solution:
    def findTargetSumWays(self, nums, S):
        if not nums:
            return 0
        num_equal_absS = 0
        if len(nums) == 1 and (nums[0] == S or nums[0] == S * -1):
                num_equal_absS = 2 if S == 0 else 1
        return self.findTargetSumWays(nums[1:], S - nums[0]) + self.findTargetSumWays(nums[1:], S + nums[0]) + num_equal_absS

# DP (DFS) with memorization
class Solution:
    def findTargetSumWays(self, nums, S):
        index = len(nums) - 1
        curr_sum = 0
        self.memo = {}
        return self.dp(nums, S, index, curr_sum)

    def dp(self, nums, target, index, curr_sum):
        if (index, curr_sum) in self.memo:
            return self.memo[(index, curr_sum)]

        if index < 0 and curr_sum == target:
            return 1
        if index < 0:
            return 0

        positive = self.dp(nums, target, index - 1, curr_sum + nums[index])
        negative = self.dp(nums, target, index - 1, curr_sum + -nums[index])

        self.memo[(index, curr_sum)] = positive + negative
        return self.memo[(index, curr_sum)]

A = Solution()
nums = [25,29,23,21,45,36,16,35,13,39,44,15,16,14,45,23,50,43,9,15]
S = 32
print(A.findTargetSumWays(nums, S))
