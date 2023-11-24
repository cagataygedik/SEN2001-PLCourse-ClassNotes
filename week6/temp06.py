def f1(a, b, c):
    print(a ** b + c ** 2)


f1(5, 3, 10)  # 225
f1(a=5, b=3, c=10)  # 225
f1(b=3, c=10, a=5)  # 225


def f2(a=1, b=0, c=0):
    print(a ** b + c ** 2)


f2(2, 3, 4)  # 24
f2(2, 3, 0)  # 8
f2(2, 3)  # 8
f2(b=2)  # 1
f2()  # 1


def f3(a, b=10, c=50):
    print(a ** b + c ** 2)


f3(2)  # 3524


def f4():
    return 5, True, "python"


print(f4())  # (5, True, 'python')
a, b, c = f4()
print(b)  # True
print(a)  # 5
print(c)  # python