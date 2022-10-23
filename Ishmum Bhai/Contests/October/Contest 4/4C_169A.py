n, petya, vasya = map(int, input().split())
chores = list(map(int, input().split()))


chores.sort()
difference = chores[vasya] - chores[vasya - 1]
if difference == 0:
    print(0)
else:
    print(difference)