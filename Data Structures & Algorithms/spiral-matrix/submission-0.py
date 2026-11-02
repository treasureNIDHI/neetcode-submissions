class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        srow=0
        erow=m-1
        scol=0
        ecol=n-1
        out=[]
        while srow<=erow and scol<=ecol:
            for i in range(scol,ecol+1):
                out.append(matrix[srow][i])

            for i in range(srow+1,erow+1):
                out.append(matrix[i][ecol]) 
            
            if srow<erow:
                for i in range(ecol-1,scol-1,-1):
                    out.append(matrix[erow][i])
            if scol<ecol:
                for i in range(erow-1,srow,-1):
                    out.append(matrix[i][scol])
        

            srow+=1 
            scol+=1 
            erow-=1 
            ecol-=1
        return out
                
# Traverse the top row → Left to Right.
# Traverse the right column → Top to Bottom.
# Traverse the bottom row → Right to Left.
# Traverse the left column → Bottom to Top.
# Repeat for the remaining inner matrix.
      