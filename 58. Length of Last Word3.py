from typing import *

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s)-1, 0
        while i>= 0 and s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length



if __name__ == '__main__':
    array= 'anh vinh dep trai  '
    print(Solution().lengthOfLastWord(array))

    
