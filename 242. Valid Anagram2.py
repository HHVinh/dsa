from typing import *

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26
        for i in s:
           count[ord(i) - ord('a')] += 1

        for i in t:
           count[ord(i) - ord('a')] -=1

        for val in count:
            if val != 0:
                return False
        return True


if __name__ == '__main__':
    s = "listen"
    t = "silenta"
    print(Solution().isAnagram(s,t))

    
