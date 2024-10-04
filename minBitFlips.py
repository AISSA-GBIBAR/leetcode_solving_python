class Solution(object):
    # def decimalToBinary(self, decimal):
    #     binary = "" 
    #     while decimal >= 1:
    #         binary = str(decimal % 2) + binary
    #         decimal //= 2
    #     return binary  
    
    # def compareString(self, string1, string2):
    #     maxLength = max(len(string1), len(string2))
    #     string1 = string1.zfill(maxLength)
    #     string2 = string2.zfill(maxLength)
        
    #     difference = sum(1 for a, b in zip(string1, string2) if a != b)
    #     return difference
            
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        count = 0
        while start > 0 or goal > 0:
            # Increment count if the current bits differ
            if (start & 1) != (goal & 1):
                count += 1
            # Shift both numbers to the right to check the next bits
            start >>= 1
            goal >>= 1
        return count
        

solution = Solution()

start = 3
goal = 4
print(solution.minBitFlips(start, goal))

# # Left shift
# x = 11        # Binary: 1011
# shifted_left = x << 1  # Shift left by 1 bit
# print(f"Left Shift: {shifted_left}")