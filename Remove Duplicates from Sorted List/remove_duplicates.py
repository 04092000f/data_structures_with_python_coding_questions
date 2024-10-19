class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        nums[:] = [x for x in nums if not (x in seen or seen.add(x))]
        return len(nums)
