class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        N=len(s)
        i=N-1
        op=0
        while i>=0:
            if i<N-1 and roman_dict[s[i]]<roman_dict[s[i+1]]:
                op-=roman_dict[s[i]]
            else:
                op+=roman_dict[s[i]]
            i-=1
        return op
