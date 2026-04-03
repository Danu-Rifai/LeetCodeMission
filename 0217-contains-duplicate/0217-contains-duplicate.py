class Solution(object):
  def containsDuplicate(self, nums):
    mySet = set()
    for i in nums:
      if i not in mySet:
        mySet.add(i)
      else:
        return True
    
    return False