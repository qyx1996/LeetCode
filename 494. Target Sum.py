class Solution:
    def findTargetSumWays(self, nums, S):
        if nums:
            num_equal_absS = 0
            if len(nums) == 1:
                if nums == S or nums == S * -1:
                    num_equal_absS = 1
            else:
                return self.findTargetSumWays(nums[1: -1], S - nums[0]) + \
                       self.findTargetSumWays(nums[1: -1], S + nums[0]) + \
                       num_equal_absS

A = Solution()
nums = [1,1,1,1,1]
S = 3
print(A.findTargetSumWays(nums, S))
