class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=digits[0]
        for i in range(1,len(digits)):
            num=num*10+digits[i]
        num=num+1
        return [int(d) for d in str(num)]