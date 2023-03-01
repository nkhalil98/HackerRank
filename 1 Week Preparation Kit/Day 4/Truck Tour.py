def truckTour(petrolpumps):
    n = len(petrolpumps)
    tank = 0
    dist = 0
    first = 0
    for i in range(n):
        tank += petrolpumps[i][0]
        dist += petrolpumps[i][1]
        if tank < dist:
            tank = 0
            dist = 0
            first = i+1
    return first
