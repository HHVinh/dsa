from typing import *

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sumRight = sum(nums[1:])   # Tính tổng các phần tử trừ phần tử đầu
        if sumRight == 0:  # Kiểm tra nếu tổng bên phải của phần tử đầu tiên = 0
            return 0
        # Duyệt qua các phần tử từ vị trí thứ 1 đến hết dãy
        for i in range(1, len(nums)):
            sumL = sum(nums[:i])    # Tổng các phần tử trước i
            sumR = sum(nums[i+1:])  # Tổng các phần tử sau i
            if sumL == sumR:        # Nếu tổng trái bằng tổng phải
                return i            # Trả về chỉ số pivot
        return -1  # Nếu không tìm thấy pivot, trả về -1


if __name__ == '__main__':
    array= [1,7,3,6,5,6]
    print(Solution().pivotIndex(array))

    
