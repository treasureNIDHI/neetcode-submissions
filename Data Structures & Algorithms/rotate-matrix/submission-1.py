class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # out=[]
        # for i in range(len(matrix)):
        #     n_w=[]
        #     for j in range(len(matrix)):
        #         n_w.append(matrix[j][i])
        #     out.append(n_w)

        # for row in out:
        #     row.reverse()

        # matrix[:]=out
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for row in matrix:
            row.reverse()

        