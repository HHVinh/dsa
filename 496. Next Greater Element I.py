from typing import *

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            found = False  # Biến để kiểm tra đã tìm thấy phần tử lớn hơn chưa
            if num in nums2:
                for i in range(nums2.index(num)+1, len(nums2)):
                    if nums2[i] > num:
                        result.append(nums2[i])  # Thêm phần tử lớn hơn đầu tiên
                        found = True  # Đánh dấu đã tìm thấy
                        break  # Dừng vòng lặp khi tìm thấy phần tử lớn hơn
            if not found:
                result.append(-1)  # Nếu không tìm thấy, thêm -1
        return result

if __name__ == '__main__':
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    print(Solution().nextGreaterElement(nums1, nums2))

    
