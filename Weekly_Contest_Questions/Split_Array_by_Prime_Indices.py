class Solution:
    def splitArray(self, nums: List[int]) -> int:
        def is_prime(n):
            if n<2:
                return False
            for i in range(2,int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True
        sum_A = 0
        sum_B = 0

        for i in range(len(nums)):
            if is_prime(i):
                sum_A += nums[i]
            else:
                sum_B += nums[i]
        return abs(sum_A - sum_B)


    