class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sort the array in ascending order
        result = []
        
        def kSum(start, k, target, current):
            if k == 2:  # Base case: 2-sum
                left, right = start, len(nums) - 1
                while left < right:
                    total = nums[left] + nums[right]
                    if total == target:
                        result.append(current + [nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1  # Skip duplicates
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1  # Skip duplicates
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
            else:
                for i in range(start, len(nums) - k + 1):
                    if i == start or (i > start and nums[i] != nums[i - 1]):
                        kSum(i + 1, k - 1, target - nums[i], current + [nums[i]])
        
        kSum(0, 4, target, [])
        return result