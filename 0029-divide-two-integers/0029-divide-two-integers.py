class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        div=int(dividend/divisor)
        if (div==2147483648):
            return (div-1)
        else:
            return div
        
        