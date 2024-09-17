from typing import *

class Solution:
    def containsDuplicate(self, nums):
        if len(nums) == len(set(nums)):
            return False
        return True



if __name__ == '__main__':
    array= []
    print(Solution().containsDuplicate(array))

    
