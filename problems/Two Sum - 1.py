# https://leetcode.com/problems/two-sum/

class Solution:
    def __init__(self):
        pass

    def twoSum(self, nums: list, target: int) -> list:
        r = []
        for i in range(len(nums)):
            v = target - nums[i]
            tmp = nums.index(nums[i])

            nums[i] = 'used'

            if v in nums:
                return [tmp, nums.index(v)]


''' too slow due to using enumerate
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for c, v in enumerate(nums):
            v2 = target - v
            nums[c] = 'used'

            if v2 in nums:
                return [c, nums.index(v2)]

'''
