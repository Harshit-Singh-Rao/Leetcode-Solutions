class Solution:
    def myAtoi(self, s: str) -> int:
        int_min=-2**31
        int_max=2**31-1
        def parse_number(index,current_num,is_negative):
            if index >=len(s) or not s[index].isdigit():
                return current_num
            current_num=current_num*10+int(s[index])
            if not is_negative and current_num>int_max:
                return int_max
            if is_negative and current_num > 2**31:
                return 2**31
            return parse_number(index+1,current_num,is_negative)
        i=0
        n=len(s)
        while i<n and s[i]==' ':
            i+=1
        is_negative=False
        if i<n and (s[i]=='-' or s[i]=='+'):
            is_negative=s[i]=='-'
            i+=1
        result=parse_number(i,0,is_negative)
        return result if not is_negative else -result