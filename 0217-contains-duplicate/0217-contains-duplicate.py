class Solution(object):
  def containsDuplicate(self, nums):
    mySet = set(nums)
    return len(nums) != len(mySet)