class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_n=0
        pro_n=1
        while n>0:
            last_digit=n%10
            sum_n=sum_n+last_digit
            pro_n=pro_n*last_digit
            n=n//10
        return pro_n-sum_n