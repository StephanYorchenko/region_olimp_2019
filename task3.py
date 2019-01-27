n, m = map(int, input().split())
a_list, b_list = input().split(), input().split()

res = 0
action_list = []
while True:
    res += 1
    if b_list[0] == a_list[0]:
        a_list = a_list[1:]
        if not a_list:
            action_list.append('1')
            break
    if b_list[0] == a_list[0]:
        action_list.append('1')
    else:
        try:
            k = a_list.index(b_list[0])
            k_list = set(a_list[:k])
            ind = 0
            for u in k_list:
                ind = max(ind, b_list.index(u))
            b_list.insert(ind + 1, b_list[0])
            b_list = b_list[1:]
            action_list.append(str(ind+1))
        except ValueError:
            b_list.append(b_list[0])
            b_list = b_list[1:]
            action_list.append(str(n))
print(res)
print(' '.join(action_list))
