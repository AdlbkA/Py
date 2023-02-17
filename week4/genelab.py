# task 1
# def mygenerator(n):
#     for i in range(n):
#         yield i*i

# n = int(input())
# for val in mygenerator(n):
#     print(val)

# task 2

# def gener(n):
#     for i in range(n):
#         if i == 0:
#             continue
#         if i % 2 == 0:
#             yield i
# n = int(input())
# mylist = []
# for val in gener(n):
#     mylist.append(str(val))

# print(', '.join(mylist))

# task 3

# def gener(n):
#     for i in range(n):
#         if i == 0:
#             continue
#         if i % 3 == 0:
#             if i % 4 == 0:
#                 yield i

# n = int(input())
# for val in gener(n):
#     print(val)

# task 4

# def squares(a, b):
#     for i in range(a, b):
#         yield i*i

# a = int(input())
# b = int(input())
# for val in squares(a, b):
#     print(val)

# task 5

# def gener(n):
#     for i in range(n, -1, -1):
#         yield i

# n = int(input())
# for val in gener(n):
#     print(val)