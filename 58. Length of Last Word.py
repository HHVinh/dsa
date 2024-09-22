from typing import *

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = s.strip().split()
        l = len(s1[-1])
        return l




if __name__ == '__main__':
    array= '   anh vinh dep trai  '
    print(Solution().lengthOfLastWord(array))

    
