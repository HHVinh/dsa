from typing import *

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapST, mapTS = {}, {}
        for i in range(len(s)):
            value1, value2 = s[i], t[i]
            # Kiểm tra ánh xạ từ s sang t và ngược lại
            if (value1 in mapST and mapST[value1] != value2) or (value2 in mapTS and mapTS[value2] != value1):
                return False
            mapST[value1] = value2  # Thêm ánh xạ từ s sang t
            mapTS[value2] = value1  # Thêm ánh xạ từ t sang s
        return True


if __name__ == '__main__':
    array= []
    print(Solution().isIsomorphic(array))

    
