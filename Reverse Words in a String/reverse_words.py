class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split() # Convert the string into the list
        s=s[::-1] # Reverse the list
        s=' '.join(map(str,s)) # Joining all the list elements into a string using whitespace as a seperator between them
        return s
