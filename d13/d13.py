#Реализуйте аналогичную функцию fast_pow для возведения в степень
def fast_pow(x, y, res=1):
    while y > 0:
        if y == 1:
            return res * x
        if y % 2 != 0:
            res *= x
        x *= x
        y //= 2
    return res


def test_fast_pow():
    for x in range(101):
        for y in range(101):
            assert fast_pow(x, y) == x ** y
    print("passed")


test_fast_pow()

