from typing import *

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        dsTenEmail = set()
        for ptu in emails:
            if '@' not in ptu:
                continue
            ten, mien = ptu.split('@')
            ten2 = ten.split('+')[0]
            ten3 = ten2.replace('.','')
            dsTenEmail.add((ten3, mien))
        return len(dsTenEmail)
            




if __name__ == '__main__':
    array= ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    print(Solution().numUniqueEmails(array))

    
