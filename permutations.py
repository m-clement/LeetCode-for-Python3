from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Start with an empty permutation
        permutations = [[]]
        
        for num in nums:
            new_permutations = []
            
            # For each existing permutation, insert the current number at every possible position
            for perm in permutations:
                for i in range(len(perm) + 1):
                    new_permutations.append(perm[:i] + [num] + perm[i:])
            
            # Update the permutations list for the next iteration
            permutations = new_permutations
        
        return permutations
