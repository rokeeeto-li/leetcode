class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        count = 0
        newMat = []
        numR = len(mat)
        numC = len(mat[0])
        if numR*numC != r*c:
            return mat
        else:
            for raw in range(r):
                temp = []
                for column in range(c):
                    temp.append(mat[count//numC][count%numC])
                    count += 1
                newMat.append(temp)
            return newMat
