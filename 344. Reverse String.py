class Solution:
    def reverseString(self, s: List[str]) -> None:
        mid = int(len(s)/2)
        last= len(s)-1
        for i in range(0,mid):
            s[i],s[last]=s[last],s[i]
            last-=1
        return s