class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
       lenght = len(s)
       count = 0

       for i in range(lenght):
           zero = 0
           one = 0
           for j in range(i, lenght):
               if s[j] == '0':
                   zero += 1
               else:
                   one += 1
               if zero <= k or one <= k:
                   count += 1
       return count


substring = Solution()
s = "11111"
k = 1
print(substring.countKConstraintSubstrings(s, k))
