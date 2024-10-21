# from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # s_Object = Counter(s)
        # t_Object = Counter(t)
        
        s_Object = {}
        t_Object = {}
        
        # for letter in s:
        #     if letter in s_Object:
        #         s_Object[letter] += 1
        #     else:
        #         s_Object[letter] = 1
        # for letter in t:
        #     if letter in t_Object:
        #         t_Object[letter] += 1
        #     else:
        #         t_Object[letter] = 1
        
        return s_Object == t_Object

solution = Solution()
print(solution.isAnagram("ab", "a"))
