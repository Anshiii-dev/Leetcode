class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        self.haystack=haystack
        self.needle=needle
        return haystack.find(needle)
            
        