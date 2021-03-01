# time limit exceeded
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        integer = 1
        res = []
        while integer <= len(nums):
            if integer not in nums:
                res.append(integer)
            integer += 1
        return res

#
class Solution:
    def findDisappearedNumbers(self, nums):
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
        return [i + 1 for i, num in enumerate(nums) if num > 0]