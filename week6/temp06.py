def f1(a, b, c):
    print(a ** b + c ** 2)


f1(5, 3, 10)
f1(a=5, b=3, c=10)
f1(b=3, c=10, a=5)


def f2(a=1, b=0, c=0):
    print(a ** b + c ** 2)


f2(2, 3, 4)
f2(2, 3, 0)
f2(2, 3)
f2(b=2)
f2()


def f3(a, b=10, c=50):
    print(a ** b + c ** 2)


f3(2)


def f4():
    return 5, True, "python"


print(f4())
a, b, c = f4()
print(b)
print(a)
print(c)