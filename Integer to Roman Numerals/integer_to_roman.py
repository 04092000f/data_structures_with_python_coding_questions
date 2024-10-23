class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romlist = [
            ["I", 1], 
            ["IV", 4], 
            ["V", 5], 
            ["IX", 9], 
            ["X", 10], 
            ["XL", 40], 
            ["L", 50], 
            ["XC", 90], 
            ["C", 100], 
            ["CD", 400], 
            ["D", 500], 
            ["CM", 900], 
            ["M", 1000]
        ]
        
        res = ""
        for sym, val in reversed(romlist):  # Reverse to start with the largest values 1st to build an efficient conversion algorithm
            count = num // val # Count how many strings will be added in the res
            if count>0: # If this greater than 0
                res += sym * count # Do the string mult using count in order 
                num %= val # Move to next digit
        return res
