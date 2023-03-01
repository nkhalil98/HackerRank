def gridChallenge(grid):
    n = len(grid)
    m = len(grid[0])
    sorted_grid = []
    for word in grid:
        sorted_grid.append(''.join(sorted(word)))
    columns = []
    for i in range(m):
        column = []
        for j in range(n):
            column.append(sorted_grid[j][i])
        columns.append(column)
    for column in columns:
        if column != sorted(column):
            return 'NO'
    return 'YES'
