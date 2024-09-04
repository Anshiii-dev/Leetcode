class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        self.haystack=haystack
        self.needle=needle
        if self.needle in haystack:
            index=haystack.find(needle)
            
        else:
            return -1    
        return index