class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        lst = sorted(nums)
        longest = 1
        cnt = 1

        for i in range(1, len(lst)):
            if lst[i] == lst[i - 1]:
                continue
            elif lst[i] == lst[i - 1] + 1:
                cnt += 1
            else:
                longest = max(longest, cnt)
                cnt = 1

        longest = max(longest, cnt)

        return longest