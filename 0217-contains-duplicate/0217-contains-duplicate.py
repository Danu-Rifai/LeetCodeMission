class Solution(object):
  def containsDuplicate(self, nums):
    mySet = set()
    duplikat = set()
    for i in nums:
      if i not in mySet:
        mySet.add(i)
      else:
        duplikat.add(i)
      
    if duplikat:
      return True
    else:
      return False
    
    return status