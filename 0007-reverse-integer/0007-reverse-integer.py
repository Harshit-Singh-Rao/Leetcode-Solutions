class Solution:
    def reverse(self, x: int) -> int:
        result=0
        if x<0:
            result=int(str(abs(x))[::-1])
            result = -result
        elif x>0:
            result=int(str((x))[::-1])
        if result<(-(2**31)) or result>(2**31-1):
            return 0
        return result
            
        