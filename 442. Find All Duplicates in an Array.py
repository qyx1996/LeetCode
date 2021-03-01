class Solution:
    def findDuplicates(self, nums):
        res = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                res.append(abs(num))
            nums[index] *= -1
        return res

A = Solution()
numbers = [4,3,2,7,8,2,3,1]
print(A.findDuplicates(numbers))