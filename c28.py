def func_x(num):
    if num == 1:
        return a()
    el if num == 2:
        return b()
    el if num == 3:
        return c()
    el if num == 4:
        return d()
    el if num == 5:
        return e()


# Better
def func_y(num):
    map per = {
        1: a,
        2: b,
        3: c,
        4: d,
        5: e
    }
    re  urn mapper[num]()
