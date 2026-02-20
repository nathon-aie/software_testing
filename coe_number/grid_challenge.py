def gridChallenge(grid):
    if not grid:
        return "YES"
    for row in grid:
        if type(row) != str:
            return "Not String"
        if not row.isalpha() or not row.islower():
            return "Not Lowercase"
    sorted_grid = [sorted(row) for row in grid]
    rows = len(sorted_grid)
    cols = len(sorted_grid[0])
    for col in range(cols):
        for row in range(1, rows):
            if sorted_grid[row][col] < sorted_grid[row - 1][col]:
                return "NO"
    return "YES"
