'''
print() -> executes the statement inside
print(str)
print(int)
print("hello", name)
print(....., end="", sep="")
print(....., sep="", end="")
input()
input("enter a number") -> returns the users input
type(a) -> returns the type of a
int(str) -> returns the incoming str to int
range(stop) -> returns a list from [0, stop)
range(start, stop) -> returns a list from [start, stop) step=1
range(start, stop, step) -> returns a list from [start, stop) increasing with stepsize

randint(min, max) -> returns a random number between [min, max]
sqrt(f) -> returns the sqrt of f
'''

i = 0
while i < 3:  # 3 < 3?
    print("hi with i:", i)
    i += 1
print("the last i:", i)

'''
hi with i: 0
hi with i: 1
hi with i: 2
the last i: 3
'''

print("-------")

for j in range(3):  # [0,1,2]
    print("hi with j:", j)
print("the last j:", j)

'''
hi with j: 0
hi with j: 1
hi with j: 2
the last j: 2
'''

print("-------")

for k in [0, 1, 2]:  # [0,1,2]
    print("hi with k:", k)
print("the last k:", k)

'''
hi with k: 0
hi with k: 1
hi with k: 2
the last k: 2
'''

