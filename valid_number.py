class Solution:
    def isNumber(self, s: str) -> bool:
        # Define the state transition table
        states = [
            {" ": 0, "digit": 2, ".": 4, "sign": 1},
            {"digit": 2, ".": 4},
            {"digit": 2, ".": 3, "e": 5, " ": 8},
            {"digit": 6, "e": 5, " ": 8},
            {"digit": 6},
            {"sign": 7, "digit": 9},
            {"digit": 6, "e": 5, " ": 8},
            {"digit": 9},
            {" ": 8},
            {"digit": 9, " ": 8}
        ]
        
        state = 0
        for c in s:
            if c.isdigit():
                trans = "digit"
            elif c in "+-":
                trans = "sign"
            elif c in "eE":
                trans = "e"
            elif c in ". ":
                trans = c
            else:
                return False
            state = states[state].get(trans, -1)
            if state == -1:
                return False
        
        # Only the following states are valid end states
        return state in [2, 3, 6, 8, 9]