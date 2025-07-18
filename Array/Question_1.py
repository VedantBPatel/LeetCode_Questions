#Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dct = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dct:
                return [dct[diff],i]
            else:
                dct[nums[i]] = i