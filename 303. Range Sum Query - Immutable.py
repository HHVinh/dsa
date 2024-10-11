from typing import List  # Nhập List từ thư viện typing

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums  # Lưu trữ danh sách nums vào thuộc tính của đối tượng
        
    def sumRange(self, left: int, right: int) -> int:
        nums = self.nums  # Lấy danh sách nums
        result = 0  # Khởi tạo biến để lưu tổng
        
        # Duyệt qua từng chỉ số từ left đến right (bao gồm cả right)
        for i in range(left, right + 1):
            result += nums[i]  # Cộng dồn giá trị vào result

        return result 

if __name__ == '__main__':
    # Khởi tạo danh sách các số nguyên
    nums = [-2, 0, 3, -5, 2, -1]
    numArray = NumArray(nums)  # Tạo đối tượng NumArray với danh sách nums

    # Gọi phương thức sumRange và in kết quả
    print(numArray.sumRange(0, 2))  # Kết quả: 1 (Tổng: -2 + 0 + 3)
    print(numArray.sumRange(2, 5))  # Kết quả: -1 (Tổng: 3 + (-5) + 2 + (-1))
    print(numArray.sumRange(0, 5))  # Kết quả: -3 (Tổng: -2 + 0 + 3 + (-5) + 2 + (-1))

   
