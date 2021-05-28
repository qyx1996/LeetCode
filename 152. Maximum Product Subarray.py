class Solution:
    def maxProduct(self, A):
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)

class Solution:
    def maxProduct(self, nums):
        locMin = locMax = glo = nums[0]
        for num in nums[1:]:
            locMin, locMax = min(locMin * num, num, locMax * num), max(locMin * num, num, locMax * num)
            glo = max(glo, locMax)
        return glo

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return
        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res
