class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        queue = deque()
        count = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    count += 1
        
        if count == 0:
            return 0

        min = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue and count > 0:
            min += 1
            for i in range(len(queue)):
                r,c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        count -= 1
                        queue.append((nr, nc))

        return min if count == 0 else -1

