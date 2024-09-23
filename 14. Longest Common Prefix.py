from typing import *

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        minLenght = min([len(word) for word in strs])
        if minLenght < 1:
            return result
        for i in range(minLenght):
            for s in strs:
                    if s[i] != strs[0][i]:
                        return result
            result += strs[0][i]
        return result
        




if __name__ == '__main__':
    array= ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(array))

    
