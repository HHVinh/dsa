from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if i + j == target:
                    return i, j
        return []

# Kiểm tra với ví dụ
if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    target = 9
    print(Solution().twoSum(array, target))

    
