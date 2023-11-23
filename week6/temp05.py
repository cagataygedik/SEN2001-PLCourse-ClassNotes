a = 1
b = 10
c = 5

print(a, b, c)
print(a, b, c, sep=" ", end="\n")
print(a, b, c, sep="-", end="\t")
print(a, b, c, end="\t", sep="-")
print("finished")


def f1(a, b, c):
    print(a ** b + c ** 2)


f1(5, 3, 10)
# f1(5, 3)
# f1(5)
