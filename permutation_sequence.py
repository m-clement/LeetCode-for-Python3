class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Helper function to calculate factorial
        def factorial(num):
            if num == 0:
                return 1
            return num * factorial(num - 1)
        
        nums = [str(i) for i in range(1, n+1)]
        result = ''
        
        while n > 0:
            fact = factorial(n-1)
            index = (k-1) // fact
            result += nums[index]
            nums.pop(index)
            k = k % fact
            n -= 1
            
        return result
