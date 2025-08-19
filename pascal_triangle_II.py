class Solution(object):
    def getRow(self, rowIndex):
        p=[]
        for i in range(rowIndex+1):
            m=[]
            for j in range(i+1):
                if j==0 or j==i:
                    m.append(1)
                else:
                    m.append(p[i-1][j-1]+p[i-1][j])
            p.append(m)
        return p[rowIndex]