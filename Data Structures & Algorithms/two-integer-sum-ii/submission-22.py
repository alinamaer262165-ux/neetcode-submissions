class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lst=[]
        for i in range(len(numbers)):
            other = target-numbers[i]
            if (other in numbers):
                idx = numbers.index(other, i + 1) if other == numbers[i] else numbers.index(other)
                return [i + 1, idx + 1]
        return []