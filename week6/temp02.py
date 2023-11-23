a = list(range(10))
a = [i**3 for i in range(10)]
a = a + ["hi"] * 2
print(a)
a[0] = "berkay"
a[len(a) - 1] = "ilgin"
print(a)
a.pop(5)
print(a)
print(a.count("Berkay"))
print("Berkay" in a)
a[3] = "berkay"
a[5] = "berkay"
print(a)
while "berkay" in a:
    a.remove("berkay")
print(a)
if "berkay" in a:
    a.remove("berkay")

print(a[2:6])  # [2...6)
print(a[:])  # [0, len(a))
print(a)
print(a[0:len(a)])
print(a[5:])
print(a[:5])
print(a[6:1000000])
print(a[2:7])
print(a[2:7:1])
print(a[2:7:2])
print(a[::-1])
a = list(range(1, 100, 7))
a.sort()
a.reverse()
print(a)
print(sum(a))
print(min(a))
print(max(a))
# lists [], tuples (), dictionary {key:values}, set
