from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for index , value  in enumerate(nums):
                complement = target - value
                if complement in hashMap:
                    return [hashMap[complement], index]
                hashMap[value] = index
            
        return []


# Kiểm tra với ví dụ
if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    target = 9
    print(Solution().twoSum(array, target))

    
