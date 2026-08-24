class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(4):
            if mat == target:
                return True
            flipped_map = mat[::-1]
            transpose = zip(*flipped_map)
            mat = [list(row) for row in transpose]
        return False