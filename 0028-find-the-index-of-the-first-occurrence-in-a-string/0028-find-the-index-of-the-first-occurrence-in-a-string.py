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
            return index
        else:
            return -1    
        