from typing import *

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count





if __name__ == '__main__':
    array= [1,2,3,4,2,0,2]
    val = 2
    print(Solution().removeElement(array, val))

    
