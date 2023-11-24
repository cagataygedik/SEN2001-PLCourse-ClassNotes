a = list(range(10))
a = [i ** 3 for i in range(10)]
print(a)  # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

a = a + ["hi"] * 2
print(a)  # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 'hi', 'hi']

a[0] = "berkay"
print(a)  # [berkay, 1, 8, 27, 64, 125, 216, 343, 512, 729, 'hi', 'hi']

a[len(a) - 1] = "ilgin"
print(a)   # [berkay, 1, 8, 27, 64, 125, 216, 343, 512, 729, 'hi', 'hi', 'ilgin']

a.pop(5)
print(a)   # ['berkay', 1, 8, 27, 64, 216, 343, 512, 729, 'hi', 'ilgin']

print(a.count("Berkay"))  # 0

print("Berkay" in a)  # false

a[3] = "berkay"
a[5] = "berkay"
print(a)  # ['berkay', 1, 8, 'berkay', 64, 'berkay', 343, 512, 729, 'hi', 'ilgin']

while "berkay" in a:
    a.remove("berkay")
print(a)  # [1, 8, 64, 343, 512, 729, 'hi', 'ilgin']

if "berkay" in a:
    a.remove("berkay")

print(a[2:6])  # [2...6) -> [64, 343, 512, 729]

print(a[:])  # [0, len(a)) -> [1, 8, 64, 343, 512, 729, 'hi', 'ilgin']

print(a[0:len(a)])  # [1, 8, 64, 343, 512, 729, 'hi', 'ilgin']

print(a[5:])  # [729, 'hi', 'ilgin']

print(a[:5])  # [1, 8, 64, 343, 512]

print(a[6:1000000])  # ['hi', 'ilgin']

print(a[2:7])  # [64, 343, 512, 729, 'hi']

print(a[2:7:1])  # [64, 343, 512, 729, 'hi']

print(a[2:7:2])  # [64, 512, 'hi']

print(a[::-1])  # ['ilgin', 'hi', 729, 512, 343, 64, 8, 1] (reversing the list)

print("--------------------------------------------------------------------------")

a = list(range(1, 100, 7))
print(a)  # [1, 8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99]

'''
a.sort()
print(a)
'''

a.reverse()
print(a)  # [99, 92, 85, 78, 71, 64, 57, 50, 43, 36, 29, 22, 15, 8, 1]

print(sum(a))  # 750
print(len(a))  # 15
print(sum(a) / len(a))  # 50.0
print(min(a))  # 1
print(max(a))  # 99
# lists [], tuples (), dictionary {key:values}, set
