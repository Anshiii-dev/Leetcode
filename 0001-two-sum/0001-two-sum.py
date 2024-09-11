class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index=[]
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i]+nums[j]==target:
                  if i or j not in index:
                    if i!=j:
                      index.append(i)
                      index.append(j)
                      return index 
                      break
                   
                    