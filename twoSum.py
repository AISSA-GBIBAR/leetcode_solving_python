class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
                
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                print(seen)
                return [seen[complement], i]
            seen[num] = i
        
    
solution = Solution()
print(solution.twoSum([3,2,4], 6))


# [3,2,3]
# [-1,-2,-3,-4,-5]
# -8
# [150,24,79,50,88,345,3]
# [1,3,4,2]