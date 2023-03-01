def superDigit(n, k):
        while len(n) > 1:
            res = 0
            for digit in n:
                res += int(digit)
            n = str(res)
        num = n*k
        while len(num) > 1:
            res = 0
            for digit in num:
                res += int(digit)
            num = str(res)
        return int(num)
