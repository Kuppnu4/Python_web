def add(a, b):
    return a + b


def add_c(a, b, cb):  # when we don't know how much time will take the performance
    r = a + b
    cb(r)


if __name__ == '__main__':
    r = add(2, 2)
    print(r)

    add_c(2, 2, print)
