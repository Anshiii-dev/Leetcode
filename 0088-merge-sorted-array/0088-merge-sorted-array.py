class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        dummy=[0]*(m+n)
        for i in range(len(dummy)):
         if i<m:
          dummy[i]=nums1[i]
         elif i>m-1:
          dummy[i]=nums2[len(dummy)-i-1]
        for i in range(len(nums1)): 
          nums1[i]=dummy[i]
        nums1.sort()
        
        