class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        start_color = image[sr][sc]

        if start_color == color:
            return image

        row = len(image)
        col = len(image[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= row or c >= col or image[r][c] != start_color:
                return 

            image[r][c] = color

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)

        return image