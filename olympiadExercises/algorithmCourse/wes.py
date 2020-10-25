amount_of_sets = int(input())  # z
results = []


def nwd(_ca_amount, _jump_len):
    if _ca_amount < _jump_len:
        temp = _ca_amount
        _ca_amount = _jump_len
        _jump_len = temp
    if _jump_len == 0:
        return _ca_amount
    return nwd(_jump_len, _ca_amount % _jump_len)


for i in range(amount_of_sets):
    nd = input().split()
    ca_amount = int(nd[0])  # n
    jump_len = int(nd[1])  # d
    results.append(int(ca_amount / nwd(ca_amount, jump_len)))

for i in range(len(results)):
    print(results[i])
