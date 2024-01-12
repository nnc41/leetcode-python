# use BUCKET SORT
# indeces are the fequency of elements of input array
# values are the elements of input array 

# create hashmap num:count
# create a list of lists length of nums which: 
   # index is count of elements
   # values is elements
# loop through nums update hashmap num:count
# loop through hashmap num:count update a list of lists
# create a list of result
# go over an updated list of lists from last to start to update result
# return if len of result = k, return result

class Solution:
  def topKfreqEle(self, nums, k):
    
    count = {}
    fre = [[] for i in range(len(nums) + 1)]
    
    for num in nums:
      count[num] = 1 + count.get(num, 0)
      
    for num, count in count.items():
      fre[count].append(num)
      
    res = []
    for i in range(len(fre) - 1, 0, -1):
      for n in fre[i]:
        res.append(n)
        if len(res) == k:
          return res

solution_instance = Solution()
nums = [1, 1, 2, 2, 4, 4, 4, 4, 8, 9, 9, 9, 9, 9]
k = 2
result = solution_instance.topKfreqEle(nums, k)
print(result)
      
    