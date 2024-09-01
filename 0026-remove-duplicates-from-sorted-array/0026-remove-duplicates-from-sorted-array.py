class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i=0
        while i <len(nums):
            j=i+1
            while j <len(nums):
                if nums[i]==nums[j]:
                    nums.remove(nums[j])
                else:
                    j+=1
            i+=1
        return i+1   
                 


        