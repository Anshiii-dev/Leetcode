class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)  # handle cases where k > len(nums)
        b = nums[-k:] + nums[:-k]
        for i in range(len(nums)):
            nums[i] = b[i]