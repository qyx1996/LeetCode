class Solution:
    def maxProduct(self, A):
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)

    def maxProduct(self, nums):
        locMin = locMax = glo = nums[0]
        for num in nums[1:]:
            locMin, locMax = min(locMin * num, num, locMax * num), max(locMin * num, num, locMax * num)
            glo = max(glo, locMax)
        return glo