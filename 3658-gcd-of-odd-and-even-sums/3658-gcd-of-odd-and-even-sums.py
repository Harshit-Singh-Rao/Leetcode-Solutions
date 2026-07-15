class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        listodd=[]
        listeven=[]
        for x in range(1,2*n+1):
            if x%2==0:
                listeven.append(x)
            elif x%2==1:    
                listodd.append(x)
        sumOdd=sum(listodd)
        sumEven=sum(listeven)
        return math.gcd(sumOdd,sumEven)