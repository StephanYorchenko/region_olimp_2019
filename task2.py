k = int(input())
if k < 0:
    for i in range(1, int(abs(k)**0.5)):
        if not abs(k) % i:
            z = abs(k) / i
            if not (i - z) % 2:
                b = int((z - i) / 2)
                print(b)
                exit()
elif k >= 0:
    if not (k**0.5) % 1:
        print(int(k**0.5))
        exit()
    else:
        for r in range(1, int(k**0.5)):
            if not (k % r):
                z = k / r
                if not (r - z) % 2:
                    b = (r - z) / 2
                    print(int((k + int(b)**2)**0.5))
                    exit()
print('none')
