# goal: mapping character count to list of Anagram

# create a hashmap ( defaultdict(list) )
# loop through each string in the list of strings
# count the frequency of each character in each string and make  character count strings
  # the same strings will have the same character count strings
  # character count string with is a tuple is the key in the hashmap
  # the string in the list of string is value

# return the values in the hashmap

class Solution:
    def grpAna(self, strs):
        res = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            # Convert the count list to a tuple
            key = tuple(count)
            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]

        return list(res.values())

# Example usage:
solution_instance = Solution()
strs = ["eat", "tea", "cat", "tac", "lat"]
result = solution_instance.grpAna(strs)
print(result)
