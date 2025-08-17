class Solution(object):
    def generate(self, numRows):
        p=[]
        for i in range(0,numRows):
            m=[]
            for j in range(0,i+1):
                if i==0:
                    m.append(1)
                elif i==1:
                    m.append(1)
                elif j==0:
                    m.append(1)
                elif j==i:
                    m.append(1)
                else:
                    m.append(p[i-1][j-1]+p[i-1][j])
            p.append(m)
        return p

            
                
# or 
# class Solution(object):
#     def generate(self, numRows):
#         p = []
#         for i in range(numRows):
#             m = []
#             for j in range(i + 1):
#                 if j == 0 or j == i:
#                     m.append(1)
#                 else:
#                     m.append(p[i-1][j-1] + p[i-1][j])
#             p.append(m)
#         return p