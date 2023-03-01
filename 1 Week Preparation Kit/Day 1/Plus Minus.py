def plusMinus(arr):
    n = len(arr)
    pos = 0
    neg = 0
    zero = 0
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1
    print(round(pos/n, 6))
    print(round(neg/n, 6))
    print(round(zero/n, 6))
