# create a hashset
# loop through num in list
# check if num in hashset
# if yes, return true
# if no, put num in hashset

class Solution:
    def containsDuplicate(self, nums):
        # Create an empty hash set to store unique elements
        hashset = set()

        # Loop through the elements in the input list 'nums'
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)
        return False
      
# Create an instance of the Solution class
solution_instance = Solution()

# Example list of integers
nums_list = [1, 2, 3, 4, 1]  # This list contains a duplicate (1)

# Call the containsDuplicate method using the instance
result = solution_instance.containsDuplicate(nums_list)

# Display the result
print("Does the list contain duplicates?", result)