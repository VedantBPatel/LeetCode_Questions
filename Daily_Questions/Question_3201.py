#Find the Max Lenght of Valid Subsequence 1
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        
        # n_even = 0
        # n_odd = 0
        # n_odev = 1
        # cur_parity = nums[0] % 2
        # for i in nums:
        #     if i%2 == 0:
        #         n_even += 1
        #     else:
        #         n_odd += 1
        #     if i%2 != cur_parity:
        #         n_odev += 1
        #         cur_parity = 0 if cur_parity else 1
        # return max(n_odd,n_even,n_odev)
        
        
        
        
        
        
        
        
        
        
        
        
        count_even=0
        count_odd=0
        count_altr=1
        for i in nums:
            if i % 2 ==0:
                count_even+=1
            else:
                count_odd+=1
        parity=nums[0]%2
        
        for i in range(1,len(nums)):
            curr_parity=nums[i] % 2
            if curr_parity!=parity:
                count_altr+=1
                parity=curr_parity
        return max(count_even,count_odd,count_altr)
                