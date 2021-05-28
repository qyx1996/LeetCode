class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        i = 1
        res = None
        for idx,v in enumerate(self.nums):
            if v == target:
                if random.randint(1, i) == 1:   # 取1的概率为1/i
                    res = idx
                i += 1
        return res