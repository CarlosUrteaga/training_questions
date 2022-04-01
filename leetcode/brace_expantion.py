"""
input is a string, where we have curly braces, 
can we have invalid brases?
ans = [
{}{}

we will iterate over each element, so we can use a while, 
i index
stack = 
tmp = 
"""
class Solution:
    def expand(self, s: str) -> List[str]:
        ans = []
        queue = []
        if len(s)==0:
            return ans
        i = 0
        while i<len(s):
            if s[i]=='{':
                i+=1
                queue =[]
                while s[i]!='}':
                    if s[i]!=',':
                        queue.append(s[i])
                    i+=1
                i+=1
                # empty
                if len(ans)==0:
                    for element in queue:
                        ans.append(element)
                else:
                    tmp = []
                    while len(queue):
                        ch = queue.pop(0)
                        for element in ans:
                            tmp.append(element + ch)
                    ans = tmp
                
            else:
                if len(ans)==0:
                    ans.append(s[i])
                else:
                    for j in range(0, len(ans)):
                        ans[j]= ans[j]+ s[i]
                i+=1
        ans.sort()
        return ans
"""
ans = []
queue = []

s = "{a,b}c{d,e}f"
i =0
len(s)->12

s[i]->{
i =1
queue ['a', 'b']
len(ans)-> 0

queue ['ac', 'bc']
i = 
"""
