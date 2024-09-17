from typing import *

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    
if __name__ == '__main__':
    arr = [1,2,3,4]
    print(Solution().containsDuplicate(arr))

    
