print(5 + 8)
print(5 - 8)
print(5 * 8)
print(8 / 5)
print(8 // 5)  # rounded to 1 from 1.6
print(2 ** 5)

###########################

a = 50

if a < 10:
    print("lakjsdl")
    print("lkjlksdajls")

print("lkjlksjdkla")

###########################

grade = 95

if grade > 90:
    print("A")
elif grade > 80:
    print("B")
elif grade > 70:
    print("C")
if grade > 60:
    print("D")
else:
    print("failed")

###########################

for i in range(3):  # [0, 1, 2]
    print(i)

print("the last value of i:", i)  # 2

###########################

for i in [1, 2, 5.5, True, "python"]:  # [0, 1, 2]
    print(i)

print("the last value of i:", i)  # python

###########################

'''
range(x) -> [0, x) -> range(0, x)
range(x, y) -> [x, y)
range(x, y, step) -> [x, y) update by step
'''
for i in range(40, 30, -2):
    if i % 3 == 0:
        print(i)
