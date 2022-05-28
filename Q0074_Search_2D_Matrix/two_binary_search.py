class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lr, rr, lc, rc = 0, len(matrix)-1, 0, len(matrix[0])-1
        while lr< rr:
            mid = (lr+rr)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                if matrix[mid][-1] == target:
                    return True
                elif matrix[mid][-1] > target:                    
                    lr = rr = mid
                    break
                else: lr = mid + 1
            elif matrix[mid][0] > target:
                rr = mid - 1

        while lc<=rc:
            mid = (lc+rc)//2
            if matrix[rr][mid] == target:
                return True
            elif matrix[lr][mid] < target:
                lc = mid + 1
            else:
                rc = mid - 1
        return False
