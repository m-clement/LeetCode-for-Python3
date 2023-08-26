
def plusOne(self, digits: List[int]) -> List[int]:
    # Initialize carry to 1
    carry = 1

    # Initialize index to the last element of digits
    i = len(digits) - 1

    # While index is non-negative
    while i >= 0:
        # Add carry to current digits[index]
        digits[i] += carry
        # If digits[index] is 10
        if digits[i] == 10:
            # Set digits[index] to 0
            digits[i] = 0
            # carry remains 1
        else:
            # Set carry to 0
            carry = 0
        # Decrement index
        i -= 1

    # If carry is still 1 after the loop:
        # Prepend 1 to the beginning of digits
    if carry == 1:
        digits.insert(0, 1)
    
    return digits