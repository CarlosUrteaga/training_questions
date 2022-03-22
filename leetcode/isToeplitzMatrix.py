# would be, tack first row, delete the last
# first iteratin, get   elem[1:]
# and  comparing each element or even do folo proxi [0]ist same 

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        proxy = matrix[0][1:]
        for rows in matrix:
            # proxy = [rows[0]] + proxy
            if proxy != rows[1:]:
                return False
            proxy = rows[:len(matrix[0])-1]
        return True
