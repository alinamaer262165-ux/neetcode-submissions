class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(s)
        print(s[::-1])
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return (cleaned[::-1]==cleaned)
        