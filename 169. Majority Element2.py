from typing import *

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result, count = 0, 0
        for num in nums:
            # Nếu count bằng 0, nghĩa là không có phần tử chiếm ưu thế nào
            if count == 0:
                result = num  # Gán phần tử hiện tại là phần tử chiếm ưu thế tạm thời
            # Cập nhật giá trị count
            # Nếu num bằng phần tử chiếm ưu thế (result), tăng count lên 1
            # Nếu num không bằng phần tử chiếm ưu thế, giảm count xuống 1
            count += (1 if num == result else -1)
        
        return result



            
                

if __name__ == '__main__':
    array= [1,2,2,3,3,3]
    print(Solution().majorityElement(array))

    
