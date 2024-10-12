from typing import *

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        result = []
        for n in nums:
            # Lấy giá trị tuyệt đối của nums[i] vì nó có thể đã bị đánh dấu âm trước đó
            i = abs(n) - 1  # Lấy chỉ số tương ứng với giá trị nums[i]
            nums[i] = -1 * abs(nums[i])  # Đánh dấu phần tử là âm
            
        for i, n in enumerate(nums):
            if n > 0:
                result.append(i + 1)  # Thêm số bị thiếu vào result
        return result



        

if __name__ == '__main__':
    array= [1,2,3,4,7,8,2,3,1]
    print(Solution().findDisappearedNumbers(array))

    
