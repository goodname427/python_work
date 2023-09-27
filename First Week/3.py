def gen():
    res1 = 1
    res2 = 1
    while True:
        yield res1
        res1, res2 = res2, res1 + res2


g = gen()
for i in range(10):
    print(g.__next__())
