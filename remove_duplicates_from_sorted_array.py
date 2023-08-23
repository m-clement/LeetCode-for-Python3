class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # If the list is empty or has only one element, return its length
        if not nums:
            return 0
        
        # Pointer for placing the next unique element
        i = 0
        
        # Loop through the elements in nums
        for num in nums:
            # If the current number is different from the number at pointer i
            if nums[i] != num:
                i += 1
                nums[i] = num
        
        # i + 1 is the count of unique elements
        return i + 1
