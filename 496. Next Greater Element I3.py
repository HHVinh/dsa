from typing import *

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = {}  # Từ điển lưu phần tử lớn hơn tiếp theo
        stack = []  # Stack để lưu các phần tử trong quá trình duyệt
        # Duyệt qua tất cả các phần tử trong nums2
        for num in nums2:
            # Nếu phần tử hiện tại lớn hơn phần tử trên đỉnh stack, tìm được phần tử lớn hơn
            while stack and num > stack[-1]:
                result[stack.pop()] = num
            stack.append(num)  # Đưa phần tử hiện tại vào stack
        # Những phần tử còn lại trong stack không có phần tử lớn hơn, gán giá trị -1
        while stack:
            result[stack.pop()] = -1
        # Trả kết quả cho từng phần tử trong nums1 dựa vào từ điển
        return [result[num] for num in nums1]


if __name__ == '__main__':
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    print(Solution().nextGreaterElement(nums1, nums2))

    
