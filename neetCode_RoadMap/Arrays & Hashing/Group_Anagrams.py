from collections import Counter

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        strs_dict, anagrams = {}, []
        count = 0
        
        for i in range(len(strs)):
            sorte = ''.join(sorted(strs[i]))

            if sorte in strs_dict:
                anagrams[strs_dict[sorte]].append(strs[i])
            else:
                strs_dict[sorte] = count
                anagrams.append([strs[i]])
                count += 1
        
        return anagrams

solution = Solution()

# print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams([""]))
