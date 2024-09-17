from typing import *

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       return sorted(s) == sorted(t)



if __name__ == '__main__':
    s = "listen"
    t = "silent"
    print(Solution().isAnagram(s,t))

    
