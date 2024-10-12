from typing import *

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
    # Tạo một dictionary đếm số lần xuất hiện của các ký tự cần thiết
        count = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        # Đếm số lần xuất hiện của từng ký tự trong 'balloon'
        for char in text:
            if char in count:
                count[char] += 1  
        # Tính số lượng từ "balloon" có thể tạo ra
        # 'l' và 'o' phải chia cho 2 vì mỗi từ "balloon" cần 2 ký tự này
        count['l'] //= 2
        count['o'] //= 2
        # Trả về số lần nhỏ nhất mà có thể tạo ra từ "balloon"
        return min(count.values())



if __name__ == '__main__':
    array= 'nlaebolko'
    print(Solution().maxNumberOfBalloons(array))

    
