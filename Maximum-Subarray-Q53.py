class Solution:
    def maxSubArray(self, arr):
        cur, ans = 0, 0 # cur is either 0 or sum of the previous elements, ans is the max sum found
        for n in arr:
            cur = max(cur + n, 0)
            ans = max(cur, ans)
        return ans or max(arr) # in case the array is all negative we must return maximum of the array