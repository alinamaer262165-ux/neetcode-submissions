class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lst=[]
        j=0
        while j <len(nums):
            p=1
            for i in range(len(nums)):
                if i!=j:
                    p=p*nums[i]
                else:
                    continue
            j+=1
            lst.append(p)
        return lst

        