def flippingMatrix(matrix):
    n = len(matrix)
    total = 0
    for i in range(n//2):
        for j in range(n//2):
            total += max(matrix[i][j], matrix[i][-(j+1)], matrix[-(i+1)][j], matrix[-(i+1)][-(j+1)])
    return total
