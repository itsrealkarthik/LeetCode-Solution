class Solution:
    def reverse(self, x: int) -> int:
        if(x > 2**31-1) or x==0 or (x < -2**31):
            return 0
        else:
            num=0
            temp=x
            x=abs(x)
            while x>0:
                remainder=x%10
                num=num*10+remainder
                x=x//10
            fin=int(num*(temp/abs(temp)))
            if fin > (2**31-1) or fin < (-2**31):
                return 0
            return fin