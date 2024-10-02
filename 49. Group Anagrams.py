from typing import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = DefaultDict(list)
        for ptu in strs:
            count = [0]*26
            for i in ptu:
                count[ord(i)-ord('a')] +=1
            result[tuple(count)].append(ptu)
        return result.values()





if __name__ == '__main__':
    array= ['anh', 'vinh', 'dep', 'nha', 'han', 'ped']
    print(Solution().groupAnagrams(array))

    
