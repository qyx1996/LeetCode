class Solution:
    def productExceptSelf(self, nums):
        left_product = 1
        n = len(nums)
        output = []
        for i in range(0, n):
            output.append(left_product)
            left_product = left_product * nums[i]
        right_product = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * right_product
            right_product = right_product * nums[i]
        return output