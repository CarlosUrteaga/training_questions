"""
optimized
"""
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        if k/26 ==n
            return "z"*n
        k =k-n
        number_of_z,notz = divmod(k,25)
        
        return "a"*(n-number_of_z-1) + chr(notz+ord('a')) + "z"*number_of_z


