from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        # Tạo một mảng prefix_sum với kích thước len(nums) + 1 để tính tổng tích lũy
        self.prefix_sum = [0] * (len(nums) + 1)
        
        # Tính tổng tích lũy cho mỗi phần tử trong nums
        for i in range(len(nums)):
            # prefix_sum[i + 1] = tổng từ đầu mảng đến chỉ số i
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        # Tính tổng từ chỉ số i đến j bằng cách sử dụng tổng tích lũy
        # prefix_sum[j + 1] - prefix_sum[i] sẽ cho tổng từ i đến j
        return self.prefix_sum[j + 1] - self.prefix_sum[i]

if __name__ == '__main__':
    # Khởi tạo mảng
    nums = [-2, 0, 3, -5, 2, -1]
    numArray = NumArray(nums)  # Tạo đối tượng NumArray

    # Gọi phương thức sumRange và in kết quả
    print(numArray.sumRange(0, 2))  # Kết quả: 1
    print(numArray.sumRange(2, 5))  # Kết quả: -1
    print(numArray.sumRange(0, 5))  # Kết quả: -3
   
