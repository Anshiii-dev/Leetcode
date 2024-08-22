class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        common = strs[0]
        Len = len(strs)
        
        for i in range(1, Len):
            val = strs[i]
            j = 0
            while j < len(common) and j < len(val) and common[j] == val[j]:
                j += 1
            common = common[:j]
            if not common:
                break
        
        return common

