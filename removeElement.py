class Solution(object):        
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
       
        filterNums = [x for x in nums if x != val] 
        k = len(filterNums)
        nums[:k] = filterNums
        return k

        
        # k = 0
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[k] = nums[i]
        #         k += 1  
        # return k

solution = Solution()
print(solution.removeElement([3,2,2,3], 3))

# nums = [3,2,2,3]
# val = 3
# expectedNums  = [2,2]

# k = solution.removeElement(nums, val)

# assert k == len(expectedNums)

# nums[:k] = sorted(nums[:k])

# for i in range(k):
#     assert nums[i] == expectedNums[i]
    
