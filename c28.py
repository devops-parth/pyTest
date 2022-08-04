def func_x(num):
    if num == 1:
        return a()
    elif num == 2:
        return b()
    elif num == 3:
        return c()
    elif num == 4:
        return d()
    elif num == 5:
        return e()


# Better
def func_y(num):
    mapper = {
        1: a,
        2: b,
        3: c,
        4: d,
        5: e
    }
    return mapper[num]()
