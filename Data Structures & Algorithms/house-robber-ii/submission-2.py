class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        
        nums1=nums[1:]
        n1=len(nums[1:])
        if n1==0:
            return 0
        if n1==1:
            return nums1[0]
        if n1==2:
            return max(nums1[0], nums1[1])
        dp=[0]*(n1)
        dp[0]=nums1[0]
        dp[1]=max(nums1[0],nums1[1])
        for i in range(2,n1):
            dp[i]=max(dp[i-1],dp[i-2]+nums1[i])
        out1=dp[n1-1]

        nums2=nums[:-1]
        n2=len(nums[:-1])
        if n2==0:
            return 0
        if n2==1:
            return nums2[0]
        if n2==2:
            return max(nums2[0], nums2[1])
        dp1=[0]*(n2)
        dp1[0]=nums2[0]
        dp1[1]=max(nums2[0],nums2[1])
        for i in range(2,n2):
            dp1[i]=max(dp1[i-1],dp1[i-2]+nums2[i])
        out2=dp1[n2-1]
        return max(out1,out2)


        