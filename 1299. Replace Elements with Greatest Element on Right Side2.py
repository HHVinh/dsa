from typing import *

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        l = len(arr)
        for i in range(l-1,-1,-1):
           newMax = max(rightMax, arr[i])
           arr[i] = rightMax
           rightMax = newMax
        return arr



            
            





if __name__ == '__main__':
    array= [17, 18, 5, 4, 6, 1]
    print(Solution().replaceElements(array))

    
