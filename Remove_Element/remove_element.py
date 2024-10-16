class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Use list comprehension to filter out the specified value
        nums[:] = [i for i in nums if i != val]
        # Return the new length of the modified list
        return len(nums)
