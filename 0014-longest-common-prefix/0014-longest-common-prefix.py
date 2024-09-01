class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return""
        common=strs[0]   
        for i in range(1,len(strs)):
            x=strs[i]
            j=0
            while j<len(common) and j<len(x) and common[j]==x[j]:
                j+=1
            common=common[:j]
            
            if not common:
                return "" 
        return common  
        
        