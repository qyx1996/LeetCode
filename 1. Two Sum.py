# 暴力枚举法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            minus = target - num
            if minus in nums[i+1:]:
                j = nums[i+1:].index(minus) + i + 1
                return [i, j]


# hashtable空间换时间
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []
