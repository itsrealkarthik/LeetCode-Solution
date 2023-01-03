class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        for l in zip(*strs):
            if list(l)!=sorted(l):
                count+=1
        return count

'''
strs=["abc",
      "ghu",
      "olas"]
zip(*strs)= ('a','g','o')
            ('b','h','l')
            ('c','u','a')
'''