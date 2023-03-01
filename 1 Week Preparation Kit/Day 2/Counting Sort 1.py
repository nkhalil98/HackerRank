def countingSort(arr):
    result = [0 for i in range(100)]
    for num in arr:
        result[num] += 1
    return result