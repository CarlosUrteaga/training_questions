class Solution:
    def calPoints(self, ops: List[str]) -> int:
        score_array = []
        for op in ops:
            if op.isnumeric():
                score_array.append(int(op))
            elif "-" in op:
                score_array.append(int(op))
            else:
                op = op.upper()
                if op == '+':
                    score_array.append(score_array[-2]+score_array[-1])
                elif op == 'D':
                    score_array.append(2*score_array[-1])
                elif op == 'C':
                    score_array.pop()
        return sum(score_array)
