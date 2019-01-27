l, r, a = [int(input()) for _ in range(3)]
res = 0
for j in range(l + 1, r + 1):
    for i in range(l, j):
        if not (j - i) % a:
            res += 1
print(res)
