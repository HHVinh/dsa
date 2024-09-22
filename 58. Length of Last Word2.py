from typing import *

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = s.strip()
        s2 = ''
        for i in range(len(s1)-1,-1,-1):
            if s1[i] ==' ':
                break
            s2 =  s1[i] + s2
        return len(s2)




if __name__ == '__main__':
    array= '   anh vinh dep trai  '
    print(Solution().lengthOfLastWord(array))

    
