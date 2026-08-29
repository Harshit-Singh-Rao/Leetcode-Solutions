class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        for i in s:
            if i not in ("abcdefghijklmnopqrstuvwxyz0123456789"):
                s=s.replace(i,"")
        if s==s[::-1]:
            return True
        else:
            return  False