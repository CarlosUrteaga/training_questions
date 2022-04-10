"""
use a dictionary, and keep track of the maximun numbers,
we require to count each element, and next return valuese 
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for num in nums:
            val = dictionary.get(num,0)+1
            dictionary[num] = val
        # sort
        ans = []
        for i in range(0,k):
            values = list(dictionary.values())
            mx = max(values)
            idx = values.index(mx)
            ans.append(list(dictionary.keys())[idx])
            del dictionary[list(dictionary.keys())[idx]]
        return ans
