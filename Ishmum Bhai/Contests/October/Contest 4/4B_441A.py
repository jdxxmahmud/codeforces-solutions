n, a, b = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = [2] * n

for i in a:
    res[i - 1] = 1
        
print(*res)