# 1. get the middle and we will swaping the array the lasted for the beginner, only the first middle apart
# for i in range (0, len(s)//2):
# change i j j i where = len -i 
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j = len(s)-1
        for i in range(0, len(s)//2):
            s[i], s[j] = s[j], s[i]
            j +=-1
        
