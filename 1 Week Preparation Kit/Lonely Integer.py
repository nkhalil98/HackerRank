def lonelyinteger(a):
    seen = []
    for num in a:
        if num not in seen:
            seen.append(num)
        else:
            seen.remove(num)
    return seen[0]

# another solution
def lonely(a):
    x = 0
    for num in a:
        x = x ^ num
    return x