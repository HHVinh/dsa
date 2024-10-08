from typing import *

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            for i in range(nums2.index(num) + 1, len(nums2)):
                if nums2[i] > num:
                    result.append(nums2[i])  # Thêm phần tử lớn hơn đầu tiên
                    break  # Dừng vòng lặp khi tìm thấy phần tử lớn hơn
            else:
                result.append(-1)  # Nếu không có phần tử lớn hơn, thêm -1
        return result

if __name__ == '__main__':
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    print(Solution().nextGreaterElement(nums1, nums2))

    
