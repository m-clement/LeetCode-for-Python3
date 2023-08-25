class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Place each number in its correct position
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        
        # Find the first position where the number doesn't match its index
        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1
        
        # If all numbers are in their correct positions
        return n + 1
