def gen_squares(n):
    i = 1
    while i <= n:
        yield i ** 2
        i += 1
