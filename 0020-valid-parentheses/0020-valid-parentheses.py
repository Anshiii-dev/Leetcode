class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_map = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in bracket_map:
                top=stack.pop() if  stack else '#'
                if bracket_map[char] !=top:
                    return False
            else:
                    stack.append(char)
        
        return not stack
# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         prev = None
#         while prev != s:
#             prev = s
#             s = s.replace("()", "").replace("{}", "").replace("[]", "")
        
#         return s == ""



       
