

# # Part 1
#
# grid = []
#
# with open("input15") as f:
#     for line in f:
#         grid.append(list(map(int, list(line.strip()))))
#
# numRows = len(grid)
# numCols = len(grid[0])
# edges = [[float("inf") for _ in range(numCols)] for _ in range(numRows)]
# visited = [[0 for _ in range(numCols)] for _ in range(numRows)]
#
# curr = (0, 0)
# edges[0][0] = 0
#
# while curr != (numRows-1, numCols-1):
#     for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
#         ni = di+curr[0]
#         nj = dj+curr[1]
#         if ni >= numRows or ni < 0 or nj >= numCols or nj < 0:
#             continue
#         if edges[ni][nj] == float("inf"):
#             edges[ni][nj] = edges[curr[0]][curr[1]] + grid[ni][nj]
#     shortest = float("inf")
#     next = None
#     for i in range(numRows):
#         for j in range(numCols):
#             if visited[i][j] != 1 and edges[i][j] < shortest:
#                 shortest = edges[i][j]
#                 next = (i, j)
#     # print(shortest, next)
#     visited[next[0]][next[1]] = 1
#     curr = next
#
# print(edges[numRows-1][numCols-1])
