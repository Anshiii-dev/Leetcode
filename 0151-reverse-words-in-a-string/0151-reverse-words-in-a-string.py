class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=s.split()
        dummy=""
        for  i in range(len(result)):
          dummy+=result[len(result)-i-1]
          if i< len(result)-1:
            dummy+=" "
        return dummy  