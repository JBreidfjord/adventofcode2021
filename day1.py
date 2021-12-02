with open("day1_input") as f:
    values = [int(v) for v in f.readlines()]

count = 0
for i, value in enumerate(values):
    if i == 0:
        continue

    if value > values[i - 1]:
        count += 1

window_sums = [sum((v, values[i - 1], values[i - 2])) for i, v in enumerate(values) if i > 1]
sum_count = 0
for i, window_sum in enumerate(window_sums):
    if i == 0:
        continue

    if window_sum > window_sums[i - 1]:
        sum_count += 1

print("Count:", count)
print("Sum count:", sum_count)
