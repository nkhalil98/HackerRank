def diagonalDifference(arr):
    n =len(arr)
    primary = 0
    secondary = 0

    for i in range(n):
        primary += arr[i][i]
        secondary += arr[i][-(i+1)]
    return abs(primary-secondary)
