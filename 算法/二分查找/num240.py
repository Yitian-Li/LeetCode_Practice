class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if matrix[i][0] > target: break

        possible_matrix = matrix[:i+1]
        new_m = len(possible_matrix)

        def binary_search(matrix_i, left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if matrix_i[mid] == target:
                    return True
                if matrix_i[mid] < target:
                    left += 1
                if matrix_i[mid] > target:
                    right -= 1
            return False

        for i in range(new_m):
            x =  binary_search(possible_matrix[i], 0, n - 1, target)
            if x: return True

        return False