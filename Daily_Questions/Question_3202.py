#Find the maximum length of valid subsquenece part 2
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        
        dp = [[0] * k for _ in range(k)] #[[0,0,0],[0,0,0],[0,0,0]] k=3
        result = 0
        for i in nums:
            i %= k
            for prev in range(k):
                dp[i][prev] = dp[prev][i] + 1
            result = max(result, max(dp[i]))
        return result   
        
# Prev: 0   i: 1    Dp: [[0, 0, 0], [1, 0, 0], [0, 0, 0]] 
# Prev: 1   i: 1    Dp: [[0, 0, 0], [1, 1, 0], [0, 0, 0]]
# Prev: 2   i: 1    Dp: [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
# Prev: 0   i: 1    Dp: [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
# Prev: 1   i: 1    Dp: [[0, 0, 0], [1, 2, 1], [0, 0, 0]]
# Prev: 2   i: 1    Dp: [[0, 0, 0], [1, 2, 1], [0, 0, 0]]
# Prev: 0   i: 2    Dp: [[0, 0, 0], [1, 2, 1], [1, 0, 0]]
# Prev: 1   i: 2    Dp: [[0, 0, 0], [1, 2, 1], [1, 2, 0]]
# Prev: 2   i: 2    Dp: [[0, 0, 0], [1, 2, 1], [1, 2, 1]]
# Prev: 0   i: 0    Dp: [[1, 0, 0], [1, 2, 1], [1, 2, 1]]
# Prev: 1   i: 0    Dp: [[1, 2, 0], [1, 2, 1], [1, 2, 1]]
# Prev: 2   i: 0    Dp: [[1, 2, 2], [1, 2, 1], [1, 2, 1]]
# Prev: 0   i: 1    Dp: [[1, 2, 2], [3, 2, 1], [1, 2, 1]]
# Prev: 1   i: 1    Dp: [[1, 2, 2], [3, 3, 1], [1, 2, 1]]
# Prev: 2   i: 1    Dp: [[1, 2, 2], [3, 3, 3], [1, 2, 1]]
# Prev: 0   i: 1    Dp: [[1, 2, 2], [3, 3, 3], [1, 2, 1]]
# Prev: 1   i: 1    Dp: [[1, 2, 2], [3, 4, 3], [1, 2, 1]]
# Prev: 2   i: 1    Dp: [[1, 2, 2], [3, 4, 3], [1, 2, 1]]
