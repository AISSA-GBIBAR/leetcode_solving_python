class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """        
        # for x in nums:
        #     if nums.count(x) > 1:
        #         return True
        # return False
        
        changeData = set(nums)
        return len(changeData) != len(nums)


solution = Solution()
print(solution.containsDuplicate([1,2,3,4]))
