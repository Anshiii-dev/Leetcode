class Solution(object):
    def twoSum(self, numbers, target):
      
      sum=[]
      a=numbers[0]
      for i in range(len(numbers)):
       for j in range(i+1,len(numbers)):
        if numbers[i]+numbers[j]==target:
            sum.append(i+1)
            sum.append(j+1)
            return sum
      return []