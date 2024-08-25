class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        key=k
        b=[0]*len(nums)
        c=nums[-key:]
        for i in range(len(c)):
         b[i]=c[i]
        for i in range(len(nums)-key):
         b[i+key]=nums[i]
        for i in range(len(nums)):
            nums[i]=b[i]