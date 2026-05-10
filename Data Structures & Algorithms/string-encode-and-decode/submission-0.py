class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":   # find the '#'
                j += 1
            length = int(s[i:j]) # number before '#'
            res.append(s[j+1 : j+1+length])  # extract exactly 'length' chars
            i = j + 1 + length   # move to next encoded string
        return res