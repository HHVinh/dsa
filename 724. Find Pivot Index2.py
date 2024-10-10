from typing import *

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sumAll = sum(nums)  # Tổng toàn bộ dãy
        sumLeft = 0  # Tổng của các phần tử bên trái
        for i in range(len(nums)):
            sumRight = sumAll - sumLeft - nums[i]  # Tổng bên phải = Tổng toàn bộ - Tổng bên trái - Phần tử hiện tại
            if sumLeft == sumRight:
                return i  # Nếu tổng trái bằng tổng phải, trả về chỉ số i
            sumLeft += nums[i]  # Cập nhật tổng bên trái khi xét phần tử tiếp theo
        return -1


if __name__ == '__main__':
    array= [2,1,-1]
    print(Solution().pivotIndex(array))

    
