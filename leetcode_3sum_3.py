class Solution:
    def threeSum(self, nums):
        if len(nums)==0:
            return nums
        nums.sort()
        solution=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                val=nums[i]+nums[left]+nums[right]
                if val==0 and [nums[i],nums[left],nums[right]] not in solution:
                    solution.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                elif val<0:
                    left+=1
                else:
                    right-=1
        return solution
C=Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(C.threeSum(nums))
