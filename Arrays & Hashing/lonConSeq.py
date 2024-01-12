# create a numSet of list of num
# initialize longest = 0
# loop through each num in numSet
# check of num is the start of a sequence
# if yes, initailize length = 0
# and while num + length still exist, keep increase length by 1
# after exit while loop, make longest is max(longest, length)
# return longest

class Solution:
  def longestCon(self, nums):
    numSet = set(nums) # unique num in numSet
    longest = 0
    
    for num in numSet:
      # start of sequence
      if (num - 1) not in numSet:
        length = 0
        while (num + length) in numSet:
          length += 1
        
        longest = max(longest, length)
    
    return longest

solution_instance = Solution()
nums = [0, 5 , 7, 5, 3, 3, 2, 1, 8, 9, 4, 44]
result = solution_instance.longestCon(nums)
print(result)
  
  