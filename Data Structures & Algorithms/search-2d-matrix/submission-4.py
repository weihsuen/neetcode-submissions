class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        while l<=r:
            mid1 = l + (r-l) //2
            if matrix[mid1][0] > target:
                r = mid1-1
            elif matrix[mid1][len(matrix[mid1])-1] < target:
                l = mid1+1
            else:
                break
        
        l=0
        r= len(matrix[mid1])-1
        while l<=r:
            mid2 = l + (r-l) //2
            if matrix[mid1][mid2] > target:
                r = mid2-1
            elif matrix[mid1][mid2] == target:
                return True
            else:
                l = mid2+1

        return False