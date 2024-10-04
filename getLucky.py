class Solution:
    def getLucky(self, s: str, k: int) -> int:
        letters = "abcdefghijklmnopqrstuvwxyz"
        concatenate  = ""
        for letter in s:
            index = letters.find(letter) + 1
            concatenate  += str(index)
            
        sumConcatenate = 0
        for i in range(k):
            sumConcatenate = sum(map(int, concatenate))
            concatenate = str(sumConcatenate)
        
        return sumConcatenate
            

classSolution = Solution()
print(classSolution.getLucky("leetcode", 2))

