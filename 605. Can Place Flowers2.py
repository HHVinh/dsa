from typing import *

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]
        # Duyệt qua danh sách từ vị trí 1 đến vị trí trước cuối (không xét phần thêm 0 vào cuối)
        for i in range(1, len(f) - 1):
            # Kiểm tra 3 vị trí liên tiếp (trước, hiện tại và sau) có đều bằng 0 hay không
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                # Nếu cả ba đều bằng 0, có thể trồng hoa tại vị trí hiện tại (gán giá trị f[i] = 1)
                f[i] = 1
                # Giảm số lượng hoa cần trồng đi 1
                n -= 1
        # Nếu đã trồng đủ hoặc nhiều hơn số hoa cần thiết (n <= 0), trả về True
        return n <= 0

if __name__ == '__main__':
    array = [1,0,0,0,0,0,1]
    n = 1
    print(Solution().canPlaceFlowers(array,n))

    
