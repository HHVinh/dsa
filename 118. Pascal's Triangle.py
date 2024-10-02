from typing import *

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            # Tạo một hàng mới với tất cả các giá trị ban đầu là 1
            row = [1] * (i + 1)
            
            # Tính toán các giá trị ở giữa hàng
            for j in range(1, i):  # Bỏ qua j = 0 và j = i vì chúng luôn là 1
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
            
            # Thêm hàng đã tính vào triangle
            result.append(row)
        return result

if __name__ == '__main__':
    array= 5
    print(Solution().generate(array))

    
