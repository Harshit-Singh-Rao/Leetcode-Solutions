class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        ss=s+s
        if len(goal)!=len(s):
            return False
        elif goal in ss:
            return True
        else:
            return False