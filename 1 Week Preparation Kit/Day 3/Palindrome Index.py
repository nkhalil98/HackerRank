def palindromeIndex(s):
    arr = list(s)
    n = len(s)
    
    for i in range(n):
        if(s[i] != s[(n-1)-i]):
            del arr[i]
            if arr==arr[::-1]:
                return i
            else:
                return (n-1)-i
            
    return -1
