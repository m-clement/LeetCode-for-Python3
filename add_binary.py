class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize carry to 0
        carry = 0
        
        # Initialize index to the last element of digits
        i = len(a) - 1
        j = len(b) - 1
        
        # Initialize result to empty string
        result = ''
        
        while i >= 0 or j >= 0:
            # Add carry to current digits[index]
            if i >= 0:
                carry += int(a[i])
            if j >= 0:
                carry += int(b[j])
            
            # Append the result of carry % 2 to the result string
            result = str(carry % 2) + result
            
            # Update the carry for the next iteration
            carry //= 2

            # Decrement the indices
            i -= 1
            j -= 1
        
        # If carry is still 1 after the loop, prepend 1 to the beginning of the result
        if carry == 1:
            result = '1' + result
        
        return result