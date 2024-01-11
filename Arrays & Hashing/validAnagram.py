# compare len of two strings
# if not the same, return false
# if same, keep going
# create hashmap for each string
# loop through the two strings and put character:frequency in hashmap of two strings
# loop through one string and compare the freq of the same character with the other string
# if not the same, return false
# if not hit false, return true

class Solution:
  
  def isAnagram(self, s, t):  
  
    if len(s) != len(t):
      return False
    
    # create HASHMAP to store characters and the frequency 
    # of each character in each word
    countS, countT = {}, {}
    
    for i in range(len(s)):
      countS[s[i]] = 1 + countS.get(s[i], 0)
      countT[t[i]] = 1 + countT.get(t[i], 0)
    
    # loop through each character of one word and compare 
    # its frequency to that character of another word 
    for c in countS:
      if countS[c] != countT.get(c, 0):
        return False
      
    return True
  
  # extra solution
    return sorted(s) == sorted(t)
  

# call class and function 
solution_instance = Solution()
s  = 'cat'
t = 'tac'
a = 'batman'
b = 'patman'
result = solution_instance.isAnagram(s, t)
print("Are the two words anagrams of each other?", result)

  
  