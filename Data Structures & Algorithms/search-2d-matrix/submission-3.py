class Solution:
    def bin_1d(self, l:int, r:int, matrix: List[List[int]], target: int):
        if l > r:
            return None
        mid = l + (r-l) //2
        if matrix[mid][0] > target:
            return self.bin_1d(l, mid-1, matrix, target)
        elif matrix[mid][len(matrix[mid])-1] < target:
            return self.bin_1d(mid+1, r, matrix, target)
        else:
            return matrix[mid]

    def bin_2d(self, l:int, r:int, matrix: List[int], target: int):
        if l > r:
            return False
        mid = l + (r-l) //2

        if matrix[mid] > target:
            return self.bin_2d(l, mid-1, matrix, target)
        elif matrix[mid] < target:
            return self.bin_2d(mid+1, r, matrix, target)
        elif matrix[mid] == target:
            return True
        else:
            return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 1:
            ans = matrix[0]
        else:
            ans = self.bin_1d(0, len(matrix)-1, matrix, target)
        
        if ans == None:
            return False
        else:
            return self.bin_2d(0, len(ans)-1, ans, target)