class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        Sum=[]
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    add=nums[i]+nums[j]+nums[k]
                    if add==target-1 or add ==target+1 or add==target:
                       return add;                    


        