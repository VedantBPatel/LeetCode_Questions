class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        
        #list 1 - numbers in range [1,n] not divisible by m
        #list 2 - numbers in range [1,n] divisible by m
        #sum1 - sum[list1]
        #sum2 - sum[list2]
        
        sum_d, sum_not_d = 0,0
        for i in range(1,n+1):
            if i%m != 0:
                sum_d+=i
            else:
                sum_not_d+=i
        return (sum_d-sum_not_d)