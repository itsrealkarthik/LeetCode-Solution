class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        fin=[]
        for i in nums:
            fin.append(i*i)
        fin.sort()
        return fin