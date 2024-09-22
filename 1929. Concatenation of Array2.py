from typing import *

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(2): #Lặp lại 2 lần vòng lặp sau
            for num in nums:
                result.append(num)
        return result




if __name__ == '__main__':
    array= [10,11,12]
    print(Solution().getConcatenation(array))

    
