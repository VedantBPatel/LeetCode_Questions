class Solution:
    def checkDivisibility(self, n: int) -> bool:
        t_sum = 0
        t_prod = 1
        temp = n
        while n > 0:
            t_sum += n%10
            t_prod *= n%10
            n = n//10
        return True if temp%(t_sum+t_prod)==0 else False