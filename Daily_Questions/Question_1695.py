#Maximum Erasure Value
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        run_score = 0
        max_score = 0
        left = 0
        
        for right in range(len(nums)):
            # if element already present
            while nums[right] in seen:
                seen.remove(nums[left])
                run_score-=nums[left]
                left+=1
            # if new element
            run_score+=nums[right]
            seen.add(nums[right])
            max_score=max(max_score,run_score)
        return max_score
        