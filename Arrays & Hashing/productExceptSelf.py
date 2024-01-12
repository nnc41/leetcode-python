# use prefix and postfix to update array result

# create an array result with len of nums, initialize each by 1
# set prefix to 1
# loop through each spot in array result and put prefix
# set postfix to 1
# loop through each spot in array result and multiply with postfix
# return res

class Solution:
  def productExceptSelf(self, nums):
    res = [1] * len(nums)
    
    prefix = 1
    for i in range(len(nums)):
      res[i] = prefix
      prefix *= nums[i]
    
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
      res[i] *= postfix
      postfix *= nums[i]
    
    return res
  
  
solution_instance = Solution()
nums = [1, 2, 3, 4]
result = solution_instance.productExceptSelf(nums)
print(result)


    