class Solution:
  
  def isAnagram(self, s, t):
    if len(s) != len(t):
      return False
    
    # create HASHMAP to store characters and the frequency 
    # of each character in each word
    countS, countT = {}, {}
    
    for i in range (len(s)):
      countS[s[i]] = 1 + countS.get(s[i], 0)
      countT[t[i]] = 1 + countT.get(t[i], 0)
    
    # loop through each character of one word and compare 
    # its frequency to that character of another word 
    for c in countS:
      if countS[c] != countT.get(c, 0):
        return False
      
    return True
    
  

# call class and function 
solution_instance = Solution()
s  = 'cat'
t = 'tac'
a = 'batman'
b = 'patman'
result = solution_instance.isAnagram(s, t)
print("Are the two words anagrams of each other?", result)

  
  