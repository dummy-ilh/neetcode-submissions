class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [c.lower() for c in s if c.isalnum()]
        is_pal = cleaned == cleaned[::-1]

        return is_pal