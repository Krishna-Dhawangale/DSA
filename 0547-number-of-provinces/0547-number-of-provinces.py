class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        def dfs(node: int):
            for neighbors in range(n):
                if isConnected[node][neighbors] == 1 and not visited[neighbors]:
                    visited[neighbors] = True
                    dfs(neighbors)

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                provinces += 1

        return provinces