from typing import *

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0  # Chỉ số cho chuỗi s
        t_index = 0  # Chỉ số cho chuỗi t
        
        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1  # Tăng chỉ số cho s nếu tìm thấy ký tự
            t_index += 1  # Luôn tăng chỉ số cho t
            
        return s_index == len(s)  # Kiểm tra xem đã duyệt hết s chưa

if __name__ == '__main__':
    s = 'abc'
    t = 'adbgch'
    print(Solution().isSubsequence(s, t))
    
