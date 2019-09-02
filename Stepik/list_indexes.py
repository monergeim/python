ls = [int(j) for j in input().split()]
v = int(input())
i = 0
if v not in ls:
    print("Отсутствует")
else:
    for x in ls:
        if x == v:
            print(i, " ")
        i += 1
