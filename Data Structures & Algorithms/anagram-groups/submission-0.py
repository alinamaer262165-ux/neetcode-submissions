class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = {}
        for word in strs:
            key = tuple(sorted(word))
            if key not in lst:
                lst[key]=[]
            lst[key].append(word)
        return list(lst.values())        