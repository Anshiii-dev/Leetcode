class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a=0
        j=0
        for i in range(len(s)):
            while j<len(t):
             if s[i] in t[j]:
                a+=1
                j+=1
                break
             j+=1   
        if j==len(t) and a!=len(s):
                return False 
        return True
                     

        