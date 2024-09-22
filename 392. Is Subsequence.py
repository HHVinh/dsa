from typing import *

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0

        while s and i < len(t):
            if s and t[i] == s[0]:
                s = s[1:]
            i += 1
        
        if not s:
            return True



if __name__ == '__main__':
    s = 'abc'
    t = 'adbgch'
    print(Solution().isSubsequence(s,t))

    
