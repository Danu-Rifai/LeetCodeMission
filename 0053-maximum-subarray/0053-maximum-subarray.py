class Solution(object):
  def maxSubArray(self, nums):
    currentSum = 0
    maxSum = nums[0]
    for i in nums:
      if currentSum < 0:
        currentSum = 0
      currentSum += i
      if currentSum > maxSum:
        maxSum = currentSum
    
    return maxSum