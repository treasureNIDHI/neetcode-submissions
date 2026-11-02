class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        out=[]
        for i in range(len(matrix)):
            n_w=[]
            for j in range(len(matrix)):
                n_w.append(matrix[j][i])
            out.append(n_w)

        for row in out:
            row.reverse()

        matrix[:]=out

        