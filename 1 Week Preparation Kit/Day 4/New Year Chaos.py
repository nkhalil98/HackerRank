def minimumBribes(q):
    bribes = 0
    for idx, value in enumerate(q):
        if value - (idx + 1) > 2:
            print('Too chaotic')
            return
        for j in range(max(value - 2, 0) , idx):
            if q[j] > value:
                bribes += 1
    print(bribes)
