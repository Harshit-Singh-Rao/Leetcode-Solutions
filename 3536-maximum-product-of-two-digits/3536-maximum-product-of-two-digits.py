class Solution:
    def maxProduct(self, n: int) -> int:
        l=[]
        n=str(n)
        for ch in n:
            ch=int(ch)
            l.append(ch)
        l.sort()
        return l[-1]*l[-2]