from typing import *

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Thêm biến đếm số lượng hoa có thể trồng
        count = 0
        for i in range(len(flowerbed)):
            # Kiểm tra xem vị trí hiện tại có trống không (giaTri == 0)
            # Và vị trí trước nó và sau nó cũng trống (hoặc ngoài rìa của flowerbed)
            if flowerbed[i] == 0:
                prev = flowerbed[i - 1] if i > 0 else 0  # Vị trí trước đó
                next = flowerbed[i + 1] if i < len(flowerbed) - 1 else 0  # Vị trí sau đó
                if prev == 0 and next == 0:
                    # Nếu cả ba vị trí đều trống, chúng ta có thể trồng hoa
                    flowerbed[i] = 1  # Đánh dấu vị trí này đã được trồng hoa
                    count += 1
                    if count >= n:
                        return True
        # Kiểm tra nếu số lượng hoa đã trồng đủ
        return count >= n

if __name__ == '__main__':
    array = [1,0,0,0,0,0,1]
    n = 1
    print(Solution().canPlaceFlowers(array,n))

    
