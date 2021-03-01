class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]
        for n in nums:
            ret += [r + [n] for r in ret]
        return ret