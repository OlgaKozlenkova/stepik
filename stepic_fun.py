# def modify_list(l):
#     i = 0
#     while i <= len(l) - 1:
#         if l[i] % 2 != 0:
#             l.remove(l[i])
#         else:
#             l[i] = l[i] // 2
#             i += 1
#
#
# lst = [1, 2, 3, 4, 5, 6]
# print(lst)
# modify_list(lst)
# print(lst)


def f(x):
    return x / 2


n = int(input())
d = {}
for i in range(n):
    x = int(input())
    if x in d:
        print(d[x])
    else:
        d[x] = f(x)
        print(d[x])
