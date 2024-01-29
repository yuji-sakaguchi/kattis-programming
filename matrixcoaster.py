#MAX_ROLLER_COASTERS = 101
MAX_TIME = 25001

#fun_matrix = [[0] * MAX_TIME for _ in range(MAX_ROLLER_COASTERS)]
fun_matrix = [[0] * MAX_TIME for _ in range(2)]

def calculate_fun(a, b, k):
    r = k - 1
    return a - r**2 * b

def fill_fun_matrix(roller_coasters):
    num_roller_coasters = len(roller_coasters)
    for coaster_idx in range(1, num_roller_coasters + 1):
        a, b, t = roller_coasters[coaster_idx - 1]
        cumulative_fun_values = [0] * 36
        k = 1
        while k < len(cumulative_fun_values):
            fun_value = calculate_fun(a, b, k)
            if fun_value <= 0:
                break
            cumulative_fun_values[k] = cumulative_fun_values[k - 1] + fun_value
            k += 1
        curr_row = coaster_idx % 2
        prev_row = (coaster_idx - 1) % 2
        for time in range(1, MAX_TIME):
            max_fun_value = fun_matrix[prev_row][time]
            if not b:
                if time - t >= 0:
                    max_fun_value = max(max_fun_value, fun_matrix[curr_row][time - t] + a)
            else:
                k = 1
                while k < len(cumulative_fun_values):
                    remaining_time = time - k * t
                    if remaining_time >= 0:
                        max_fun_value = max(max_fun_value, fun_matrix[prev_row][remaining_time] + cumulative_fun_values[k])
                        k += 1
                    else:
                        break
            fun_matrix[curr_row][time] = max(max_fun_value, fun_matrix[curr_row][time - 1])

num_roller_coasters = int(input())
roller_coasters = []
for _ in range(num_roller_coasters):
    a, b, t = map(int, input().split())
    roller_coasters.append((a, b, t))
fill_fun_matrix(roller_coasters)

num_visits = int(input())
while num_visits > 0:
    visit_time = int(input())
    print(fun_matrix[num_roller_coasters % 2][visit_time])
    num_visits -= 1
