class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        fin=[]
        for i in tokens:
            if i not in {"+", "-", "*", "/"}:
                fin.append(int(i))
            else:
                r=fin.pop()
                l=fin.pop()
                if i == "+": fin.append(l+r)
                elif i == "-": fin.append(l-r)
                elif i == "*": fin.append(l*r)
                else: fin.append(trunc(l/r))
        return fin[0]