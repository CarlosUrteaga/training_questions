"""
cant start a number with 0
we can have multiple characters without numbers
iterate over each element on abbr
always compare current i with the string
if they are not equal we have a number, 
word[i] == abr[i]
convert the string to number and find if the value i position exist is the same

"""
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        idx = 0
        carry = 0
        alone = True
        for i in range(0, len(abbr)):
            if abbr[i].isdigit():
                if abbr[i]=='0' and alone :
                    return False
                else:
                    carry = carry*10 + int(abbr[i])
                    alone = False
            elif carry ==0:
                if idx>=len(word):
                    return False
                if abbr[i]== word[idx]:
                    idx +=1
                elif abbr[i]== word[idx+carry+1]:
                    carry = 0
                    idx += carry +1 
                else:
                    return False
            else:
                idx +=carry
                if idx>=len(word):
                    return False
                if word[idx] != abbr[i]:
                    return False
                idx +=1
                carry = 0
        if carry>0:
            idx +=carry
        if len(word)==idx:
            
            return True
        return False
"""
idx = 0
carry = 0
alone = True
i = 0
    abbr[0]-> "i"
    word[idx]-> "i"
    idx =1
i = 1
    abbr[1]->"1"
    carry = 1
    alone = False
i = 2
    abbr[1]->"2"
    carry = 12
    alone = False
i = 3
    abbr[1]->"i"
    carry = 1
    alone = False

"""
