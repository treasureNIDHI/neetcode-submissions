class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for num in nums:
            result ^=num
        return result
        # freq={}
        # for num in nums:
        #     freq[num]=freq.get(num,0)+1
        # for num in nums:
        #     if freq.get(num,0)==1:
        #         return num
        
                
           
        