s = input()

operator_list = []
minus_idx = 0
for i, e in enumerate(s):
    if e == "-" and not minus_idx:
        minus_idx = i
    if e == "+" or e == "-":
        operator_list.append(i)
operator_list.append(len(s))

flag = False
idx = 0
result = 0
for i in operator_list:
    if flag:
        result -= int(s[idx:i])
    else:
        result += int(s[idx:i])
    if i == minus_idx:
        flag = True
    idx = i + 1

print(result)
