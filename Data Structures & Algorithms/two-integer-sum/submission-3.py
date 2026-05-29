class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        premap = {}
        for i, n in enumerate(nums):
            dif = target - n
            if dif in premap:
                return [premap[dif], i]
            premap[n] = i
        