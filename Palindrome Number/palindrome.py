class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        reverse = 0
        temp = x
        
        while temp != 0:
            digit = temp % 10
            reverse = (reverse * 10) + digit
            temp //= 10  # Use integer division
        
        return x == reverse  # Return the comparison directly
