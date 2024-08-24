class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        self.nums=nums
        self.val=val
        for i in range(len(nums)):
            if val in self.nums:
              self.nums.remove(self.val)
        print(self.nums)
        return len(self.nums)
        