class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.split()
        s=s[-1]
        l=len(s)
        return l