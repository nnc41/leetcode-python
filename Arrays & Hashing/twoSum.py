# return two indeces in a list that sum equal given num

# create hashmap: num: index
# calculate diff of target and num
# loop through num in list to see if diff == num
# if yes, return index of diff and index of num
# if no, put num and its index in hashmap

class Solution:
  def twoSum(self, nums, target):
    prevMap = {}
  
    for i, n in enumerate(nums):
      diff = target - n
      if diff in prevMap:
        return [prevMap[diff], i]
      prevMap[n] = i
    
    
solution_instance = Solution()
nums = {1, 2, 4, 5}
target = 7
result = solution_instance.twoSum(nums, target)
print(result)
  



  
  