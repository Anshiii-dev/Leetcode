class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=0
        count=0
        for i in range(len(nums)):
            if nums[j]==nums[i]:
                count+=1
                if count>1:
                    return nums[j]
                    break
        
        



        