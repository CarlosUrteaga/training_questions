class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # memory
        dictionary = {}
        # left index
        left = 0
        # ans maximun
        mx = 0
        # we want to iterate over each element, 
        for i in range(0, len(s)):
            # get the char at i position
            tmp = dictionary.get(s[i],0)+1
            # if that char exist in the dictionary i will remove elements on my keyç
            dictionary[s[i]]=tmp
            while len(dictionary.keys())>2:
                if dictionary[s[left]]==1:
                    del dictionary[s[left]]
                else:
                    dictionary[s[left]]+=-1
                left +=1
            mx = max(mx, 1+i-left)
        return mx
