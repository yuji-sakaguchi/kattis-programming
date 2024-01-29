N = int(input())
pipe_to_parent = {}
for _ in range(N - 1):
    A, B, X, T = map(int, input().split())
    pipe_to_parent[B] = (A, X, T)
liquid = [int(k) for k in input().split()]

required_liquid = 0
for i, amount in enumerate(liquid, start=1):
    if amount == -1:
        continue
    curr = i
    while curr != 1:
        curr, percentage, superpower = pipe_to_parent[curr]
        if superpower:
            amount **= 0.5
        amount /= percentage/100 
    required_liquid = max(required_liquid, amount)
print('%.4f' % required_liquid)