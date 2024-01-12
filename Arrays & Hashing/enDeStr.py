class Solution:
  
  def encode(self, strs):
    res = ""
    for s in strs:
      res += str(len(s)) + "#" + s
    
    return res
  
  def decode(self, str):
    res, i = [], 0 # i is integer, pointer
    while i < len(str):
      j = i
      while str[j] != "#":
        j += 1
      length = int(str[i:j])
      res.append(str[j + 1 : j + 1 + length])
      i = j + 1 + length

    return res
    
solution_instance = Solution()
strs = ["cat", "dog", "mouse", "ti5#ger"]
result1 = solution_instance.encode(strs)
str_val = "3#cat3#dog5#mouse7#ti5#ger"
result2 = solution_instance.decode(str_val)
print(result1)  # Output: "3#cat3#dog5#mouse7#ti5#ger"
print(result2)  # Output: ['cat', 'dog', 'mouse', 'ti5#ger']
