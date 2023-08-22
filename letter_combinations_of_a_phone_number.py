class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_to_letters = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }
        result = []
        
        def backtrack(index, current):
            if index == len(digits):
                result.append(current)
                return
            
            for letter in digit_to_letters[digits[index]]:
                backtrack(index + 1, current + letter)
        
        backtrack(0, '')
        return result