from typing import *

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Bước 1: Khởi tạo danh sách kết quả với tất cả các giá trị ban đầu là -1
        res = [-1] * len(nums1)
        # Bước 2: Tạo từ điển để lưu chỉ số của từng phần tử trong nums1
        nums1_index = {n: i for i, n in enumerate(nums1)}
        # Bước 3: Khởi tạo stack để lưu các phần tử chưa tìm thấy phần tử lớn hơn
        stack = []
        # Bước 4: Duyệt qua từng phần tử trong nums2
        for n in nums2:
            # Bước 5: Kiểm tra và cập nhật phần tử lớn hơn cho các phần tử trong stack
            while stack and stack[-1] < n:
                val = stack.pop()  # Lấy phần tử trên đỉnh stack
                res[nums1_index[val]] = n  # Cập nhật kết quả với phần tử lớn hơn
            # Bước 6: Nếu n là phần tử trong nums1, thêm nó vào stack
            if n in nums1_index:
                stack.append(n)
        return res



if __name__ == '__main__':
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    print(Solution().nextGreaterElement(nums1, nums2))

    
