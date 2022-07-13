def add(n):
    def fn(x):
        return x + n

    return fn
    #return lambda x: x + n

add2 = add(2)
print(add2(4))

add100 = add(100)
print(add100(4))
