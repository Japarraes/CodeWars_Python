from ast import main



# What will be the Output?

# -----------------------------------
# a = max(False,-3,-4)
# b = min(a,2,7)
# print(b)

# Solution: False

# -----------------------------------
# def fun():
#     return 55 + int(55.55)

# print(fun())

# solution: 110

# -----------------------------------
# def f1():
#     x=100
#     return x

# x = f1() + 1
# print(x)

# Solution: 101

# -----------------------------------
# L = [1,2,3,4]
# for i in L[::1]:
#     print(i, end=' ')
# print("\n")
# for i in L[::-1]:
#     print(i, end=' ')

# Solution: 1 2 3 4
#           4 3 2 1

# -----------------------------------
# x = 0
# while x <= 18:
#     x = x+3
# print(x)

# Solution: 21

# -----------------------------------
# x = 0
# while x <= 18:
#     x = x+3
# print(x)

# Solution: 21

# -----------------------------------
# a = ~4 # it means -(4+1)=-5
# b = a + 4
# print(b)

# Solution: 21

# -----------------------------------
# x = ["a", "b", "c"]
# result = "".join(x)
# print(result)

# -----------------------------------
x = [0,1,3,4,5,6,7,8,9]
y = [1,3,5,6,8,9]
print(x[3:-3])
print(y[::-3])
