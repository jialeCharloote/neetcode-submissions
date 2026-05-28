class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        A = set()
        for i in range(len(nums)):
            if nums[i] not in A:
                A.add(nums[i])
            else:
                return True
        return False