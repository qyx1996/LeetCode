class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, sum = 0, 0
        sum_dict = dict()
        sum_dict[0] = 1

        for num in nums:
            sum += num
            res += sum_dict.get(sum - k, 0)
            sum_dict[sum] = sum_dict.get(sum, 0) + 1

        return res