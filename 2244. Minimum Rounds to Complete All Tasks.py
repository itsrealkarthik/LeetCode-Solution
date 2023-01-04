class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        unique=Counter(tasks)
        res=0
        for i in unique.values():
            if i==1:
                return -1
            else:
                res += ceil(i/3)
        return res
             
