from typing import *

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        dsTenEmail = set()  # Dùng set để lưu các email duy nhất
        for ptu in emails:
            if '@' not in ptu:
                continue  # Bỏ qua nếu không phải địa chỉ email hợp lệ
            ten, mien = ptu.split('@')  # Tách phần trước và sau ký tự '@'
            
            # Loại bỏ mọi thứ sau dấu '+'
            if '+' in ten:
                ten = ten.split('+')[0]
            
            # Loại bỏ dấu '.'
            ten = ten.replace('.', '')
            
            # Kết hợp lại phần local và domain rồi thêm vào set
            newEmail = ten + '@' + mien
            dsTenEmail.add(newEmail)
        
        return len(dsTenEmail)
    
if __name__ == '__main__':
    array= ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    print(Solution().numUniqueEmails(array))

    
