# class Solution:
#     def minimumDifference(self, nums: List[int]) -> int:
#         # l = len(nums)
#         # n = l//3
#         # remove_counter = 0
#         # for i in range(n*2):
#         #     if remove_counter == n:
#         #         break

from heapq import heappush, heappop, heapify
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        total_len = 3 * n

        # Min sum prefix for first 2n elements
        left_heap = []
        left_sum = 0
        left_min_sum = [0] * total_len

        for i in range(n):
            left_sum += nums[i]
            heappush(left_heap, -nums[i])  # max-heap using negative values
        left_min_sum[n - 1] = left_sum

        for i in range(n, 2 * n):
            heappush(left_heap, -nums[i])
            left_sum += nums[i]
            removed = -heappop(left_heap)  # Remove largest
            left_sum -= removed
            left_min_sum[i] = left_sum

        # Max sum suffix for last 2n elements
        right_heap = []
        right_sum = 0
        right_max_sum = [0] * total_len

        for i in range(total_len - 1, total_len - n - 1, -1):
            right_sum += nums[i]
            heappush(right_heap, nums[i])  # min-heap
        right_max_sum[total_len - n] = right_sum

        for i in range(total_len - n - 1, n - 1, -1):
            heappush(right_heap, nums[i])
            right_sum += nums[i]
            removed = heappop(right_heap)  # Remove smallest
            right_sum -= removed
            right_max_sum[i] = right_sum

        # Compare prefix and suffix sums
        res = float('inf')
        for i in range(n - 1, 2 * n):
            res = min(res, left_min_sum[i] - right_max_sum[i + 1])

        return res
