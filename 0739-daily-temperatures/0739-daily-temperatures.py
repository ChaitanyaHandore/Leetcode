class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        r = []
        for i in range(len(temperatures)):
            c = 0
            for j in range(i,len(temperatures)):
                if i==j:
                    continue
                else:
                    if temperatures[i]<temperatures[j]:
                        c+=1
                        r.append(c)
                        break
                    else:
                        c+=1

        if len(temperatures)!=len(r):
            a = len(temperatures)-len(r)
            r = r+[0]*a
        return r