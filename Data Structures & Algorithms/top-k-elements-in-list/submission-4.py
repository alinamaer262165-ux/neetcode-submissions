class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp ={}
        lst=[]
        for i in nums:
            if i not in mp:
                mp[i]=1
            else:
                mp[i]+=1
        for j,l in sorted(mp.items(),key = lambda x:x[1],reverse=True):
            lst.append(j)
            print(j)
        return lst[:k]