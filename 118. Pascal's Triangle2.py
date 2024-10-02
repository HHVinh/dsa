from typing import *

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]  # Khởi tạo hàng đầu tiên của Pascal's Triangle

        for i in range(numRows - 1):  # Duyệt qua số hàng còn lại
            temp = [0] + result[-1] + [0]  # Thêm 0 ở đầu và cuối hàng trước
            row = []  # Khởi tạo hàng mới
            for j in range(len(result[-1]) + 1):  # Duyệt qua các chỉ số của hàng
                row.append(temp[j] + temp[j + 1])  # Tính giá trị mới cho hàng
            result.append(row)  # Thêm hàng mới vào kết quả

        return result





if __name__ == '__main__':
    array= 5
    print(Solution().generate(array))

    
