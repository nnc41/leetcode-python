class Solution:
  def isAnagram(self, s, t):
    if len(s) != len(t):
      return False
    
    countS, countT = {}, {}
    
    for i in range (len(s)):
      countS[s[i]] = 1 + countS.get(s[i], 0)
      countT[t[i]] = 1 + countT.get(t[i], 0)
      
    for c in countS:
      if countS[c] != countT.get(c, 0):
        return False
      
    return True
  
solution_instance = Solution()
s  = 'cat'
t = 'tat'
a = 'abcde'
b = 'edcba'
result = solution_instance.isAnagram(s, t)
print("Are the two words anagrams of each other?", result)
  
  