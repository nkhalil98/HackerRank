def miniMaxSum(arr):
    total = sum(arr)
    without = []
    for num in arr:
        without.append(total-num)
    print(str(min(without)) + ' ' + str(max(without)))
