from typing import *

from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Tạo một đối tượng Counter để đếm số lần xuất hiện của mỗi ký tự trong chuỗi 'text'
        count_text = Counter(text)
        # Tạo một đối tượng Counter cho từ 'balloon' để biết số lần xuất hiện cần thiết của từng ký tự
        balloon = Counter("balloon")
        # Khởi tạo biến 'result' với giá trị lớn ban đầu (độ dài của chuỗi text)
        # Giá trị này sẽ được thay đổi trong quá trình tính toán, để tìm giá trị nhỏ nhất.
        result = len(text)
        
        # Duyệt qua từng ký tự trong Counter của từ 'balloon'
        for c in balloon:
            # Tính số lần có thể sử dụng ký tự 'c' trong từ 'balloon'
            # Sử dụng phép chia giữa số lần ký tự xuất hiện trong 'text' và số lần nó xuất hiện trong 'balloon'
            # Nếu ký tự 'c' không có trong 'text', Counter sẽ trả về 0 (có nghĩa không thể tạo ra thêm từ 'balloon')
            result = min(result, count_text[c] // balloon[c])
        
        return result




if __name__ == '__main__':
    array= 'nlaebolko'
    print(Solution().maxNumberOfBalloons(array))

    
