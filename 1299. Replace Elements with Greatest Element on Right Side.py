from typing import *

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        valueMax = -1  # Bắt đầu với giá trị tối thiểu

        # Lặp từ cuối danh sách về đầu = với for index in rang(5,0,-1)
        for index in range(len(arr) - 1, -1, -1):
            result.append(valueMax)  # Thêm giá trị lớn nhất đã thấy => result = -1 ngay lúc này
            valueMax = max(valueMax, arr[index])  # Cập nhật giá trị lớn nhất để đổi giá trị khác - 1

        return result[::-1]  # Đảo ngược kết quả để trả về theo thứ tự ban đầu



            
            





if __name__ == '__main__':
    array= [17, 18, 5, 4, 6, 1]
    print(Solution().replaceElements(array))

    
