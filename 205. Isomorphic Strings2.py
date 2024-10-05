from typing import *
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s_to_t = {}
        map_t_to_s = {}
        for indexs, values in enumerate(s):
            valuet = t[indexs]  # Lấy ký tự tương ứng từ chuỗi t
            # Kiểm tra ánh xạ từ s sang t
            if values in map_s_to_t:
                if map_s_to_t[values] != valuet:
                    return False
            else:
                map_s_to_t[values] = valuet
            if valuet in map_t_to_s:
                if map_t_to_s[valuet] != values:
                    return False
            else:
                map_t_to_s[valuet] = values

        return True

            

if __name__ == '__main__':
    s = 'egg'
    t = 'abd'
    print(Solution().isIsomorphic(s,t))

    
