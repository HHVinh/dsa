from typing import *

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        nums2 = set(range(1, n + 1))  # Chuyển nums2 thành set
        result = list(nums2 - set(nums))  # Trừ hai set với nhau và chuyển về list
        return result

        

if __name__ == '__main__':
    array= [1,2,3,4,7,8,2,3,1]
    print(Solution().findDisappearedNumbers(array))

    
