l, r, a = [int(input()) for _ in range(3)]
res = 0
for j in range(l + 1, r + 1):
    res += (j - l)//a
print(res)
