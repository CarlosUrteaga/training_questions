class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = 999999
        tmp = 0
        i = 0
        j = 0
        while j<len(nums):
            tmp +=nums[j]
            while tmp>=target:
                ans = min(j+1-i, ans)
                tmp+=-nums[i]
                i+=1
            j+=1
        if ans == 999999:
            return 0
        return ans
