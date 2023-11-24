a = 1
b = 10
c = 5

print(a, b, c)
print(a, b, c, sep=" ", end="\n")  # 1 10 5
print(a, b, c, sep="-", end="\t")  # 1 10 5
print(a, b, c, end="\t", sep="-")  # 1-10-5	1-10-5	finished
print("finished")


def f1(a, b, c):
    print(a ** b + c ** 2)


f1(5, 3, 10)  # 225
# f1(5, 3) -> We can't do that we have to start from the right end. c will complains
# f1(5) -> We can't do that we have to start from the right end. b & c complains.
