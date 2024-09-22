from typing import *

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = nums
        result2 = result + nums
        return result2
        


            
            





if __name__ == '__main__':
    array= [17, 18, 5, 4, 6, 1]
    print(Solution().getConcatenation(array))

    
