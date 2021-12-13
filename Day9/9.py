grid = []

def printGrid(grid):
    for row in grid:
        print(row)

with open("input9") as f:
    for line in f:
        grid.append(list(map(int, [x for x in line.strip()])))
    printGrid(grid)

riskLevel = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        lowPoint = True
        curr = grid[i][j]
        lowPoint &= curr < grid[i-1][j] if i > 0 else True
        lowPoint &= curr < grid[i][j-1] if j > 0 else True
        lowPoint &= curr < grid[i][j+1] if j < len(grid[0])-1 else True
        lowPoint &= curr < grid[i+1][j] if i < len(grid)-1 else True
        riskLevel += curr + 1 if lowPoint else 0

print(riskLevel)
