from typing import *

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        setnums = set(nums)
        result = []
        for i in range(1, n+1):
            if i not in setnums:
                result.append(i)
        return result

        

if __name__ == '__main__':
    array= [1,2,3,4,7,8,2,3,1]
    print(Solution().findDisappearedNumbers(array))

    
