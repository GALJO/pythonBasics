nq = input().split()
n = int(nq[0])
q = int(nq[1])
A = list(map(int, input().split()))
quests = []
for i in range(q):
    quests.append(tuple(map(int, input().split())))

for i in range(q):
    act_quest = quests[i]
    sum_ = 0
    for j in range(act_quest[0] - 1, act_quest[1]):
        sum_ += A[j]
    print(sum_)
