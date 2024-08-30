import random

first_board = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
second_board = []
n = 4 # (random.choice(first_board))
print(n)
for j in range(1, int(n/2 + 1)):
    for k in range(1, n + 1):
        if j + k > n + 1:
            continue
        elif n % (j + k) == 0:
            second_board.append(j)
            second_board.append(k)
result = ("".join(map(str, second_board)))
print(result)
