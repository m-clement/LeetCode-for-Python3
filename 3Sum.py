class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array in ascending order
        result = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates
            
            left, right = i + 1, len(nums) - 1
            target = -nums[i]
            
            while left < right:
                if nums[left] + nums[right] == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1  # Skip duplicates
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1  # Skip duplicates
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        
        return result