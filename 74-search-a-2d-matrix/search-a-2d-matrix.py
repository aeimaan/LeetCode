class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        mid = (top + bottom) // 2
        found = False

        if matrix[top][0] == target or matrix[bottom][0] == target: return True


        while top <= bottom and bottom-top > 1:
            if matrix[mid][0] == target: return True

            if matrix[mid][0] > target:
                bottom = mid 
            elif matrix[mid][0] < target:
                top = mid

            mid = (top + bottom) // 2



        if target > matrix[bottom][0]: index_to_look = bottom
        else: index_to_look = top

        l = 0
        r = len(matrix[index_to_look]) -1 

        mid = (l+r) // 2

        while l <= r:
            if matrix[index_to_look][mid] == target:
                return True
            if matrix[index_to_look][mid] > target: r = mid -1
            elif matrix[index_to_look][mid] < target: l = mid +1
            mid = (l+r) //2


        return False