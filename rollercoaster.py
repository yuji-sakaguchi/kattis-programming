def calculate_fun(a, b, k):
    r = k - 1
    return a - r**2 * b

def best_fun(coasters):
    for coaster_idx in range(1, N + 1):
        a, b, t = coasters[coaster_idx - 1]
        cumulative_fun = [0] * 33
        k = 1
        while k < len(cumulative_fun):
            fun_value = calculate_fun(a, b, k)
            if fun_value <= 0:
                break
            cumulative_fun[k] = cumulative_fun[k - 1] + fun_value
            k += 1
        curr_row = coaster_idx % 2
        prev_row = (coaster_idx - 1) % 2
        for time in range(1, most+1):
            max_fun = fun[prev_row][time]
            if b == 0:
                if time - t >= 0:
                    max_fun = max(max_fun, fun[curr_row][time - t] + a)
            else:
                k = 1
                while k < len(cumulative_fun):
                    remaining_time = time - k * t
                    if remaining_time >= 0:
                        max_fun = max(max_fun, fun[prev_row][remaining_time] + cumulative_fun[k])
                        k += 1
                    else:
                        break
            fun[curr_row][time] = max(max_fun, fun[curr_row][time - 1])

N = int(input())
most = 0
coasters = []
visit_time = []
for _ in range(N):
    a, b, t = map(int, input().split())
    coasters.append((a, b, t))
Q = int(input())
while Q > 0:
    visit_time.append(int(input()))
    Q -= 1    
most = max(visit_time)
fun = [[0] * (most+1) for _ in range(2)]
best_fun(coasters)
for time in visit_time:
    print(fun[N % 2][time])
