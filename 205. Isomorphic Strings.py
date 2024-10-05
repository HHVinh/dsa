from typing import *

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s_to_t = {}  # ánh xạ từ ký tự chuỗi s sang chuỗi t
        map_t_to_s = {}  # ánh xạ từ ký tự chuỗi t sang chuỗi s
        # Duyệt qua từng cặp ký tự từ s và t cùng một lúc
        for values, valuet in zip(s, t):
            # Kiểm tra ánh xạ từ s sang t
            if values in map_s_to_t:
                if map_s_to_t[values] != valuet:
                    return False
            else:
                map_s_to_t[values] = valuet
            # Kiểm tra ánh xạ từ t sang s
            if valuet in map_t_to_s:
                if map_t_to_s[valuet] != values:
                    return False
            else:
                map_t_to_s[valuet] = values  # Nếu chưa có ánh xạ, thêm vào
        return True

            

if __name__ == '__main__':
    s = 'egg'
    t = 'abd'
    print(Solution().isIsomorphic(s,t))

    
