class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_numerals = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
               ]
    
        roman = ""  # Initialize an empty string to build the Roman numeral
    
    # Iterate through the list of tuples
        for value, numeral in roman_numerals:
        # While the number is greater than or equal to the integer value
          while num >= value:
            roman += numeral  # Append the corresponding Roman numeral to the result
            num -= value  # Subtract the integer value from the number
            
        return roman  # Return the constructed Roman numeral

# Example usage
        