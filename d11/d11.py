def naive_mul(x, y):
    if((0 <= x < 100) and (0 <= y < 100)):
        if(x == 0 or y == 0):
            return 0
        else:
            a = x
            for _ in range(y - 1):
                a += x
            assert (x * y) == a, "check mistakes"
            return a
   


print(naive_mul(5,5))
