def lonelyinteger(a):
    seen = set()
    for num in a:
        if num not in seen:
            seen.add(num)
        else:
            seen.remove(num)
    return list(seen)[0]

# another solution
def lonely(a):
    x = 0
    for num in a:
        x = x ^ num
    return x