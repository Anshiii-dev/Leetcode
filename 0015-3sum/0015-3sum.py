class Solution(object):
 def threeSum(self,nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            if -(nums[i] + nums[j]) in nums[j + 1:]:
                result.append([nums[i], nums[j], -(nums[i] + nums[j])])
    return result