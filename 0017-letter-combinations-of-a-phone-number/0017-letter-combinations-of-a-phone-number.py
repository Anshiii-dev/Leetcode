class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        keypad_mapping = {
    "1": ["◯", "↻"],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
    "*": ["*", "+"],
    "0": ["0", "⏎"],
    "#": ["⇧", "#"]}

        if digits=="":
         return []
        result=[""]
        for char in digits:
         letters=keypad_mapping.get(char,[])
         temp=[]
         for data in result:
            for letter in letters:
                temp.append(data+letter)
            result=temp
        return result

        


