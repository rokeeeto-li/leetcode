class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []
        for i in range(numRows):
            row = [1]*(i+1)
            if i > 1:
                for j in range(i-1):
                    row[j+1] = tri[-1][j] + tri[-1][j+1]
            tri.append(row)
        return tri
