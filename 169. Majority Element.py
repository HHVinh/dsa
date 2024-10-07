from typing import *

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}  # Tạo một dictionary để lưu số lần xuất hiện của mỗi phần tử

        for num in nums:
            if num in count_dict:
                count_dict[num] += 1  # Tăng số lần xuất hiện lên 1
            else:
                count_dict[num] = 1  # Nếu phần tử chưa có, gán số lần xuất hiện là 1

        result = max(count_dict, key=count_dict.get)
        if count_dict[result] >= len(nums) // 2:
            return result
        else:
            return None


            
                

if __name__ == '__main__':
    array= [1,2,2,3,3,3]
    print(Solution().majorityElement(array))

    
