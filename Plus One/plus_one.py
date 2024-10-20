class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Convert the list of digits to a string, then to an integer
        number = int(''.join(map(str, digits)))
        # Increment the number by one
        number += 1
        # Convert the incremented number back to a list of digits
        return [int(digit) for digit in str(number)]
