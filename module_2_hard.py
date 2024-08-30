import random
first_board = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
second_board = []
n =  random.choice(first_board)
print(n)
for j in range(1, n):
    for k in range(j+1, n):
       if n % (j + k) == 0:
            second_board += str(j) + str(k)
password = ("".join(map(str, second_board)))
print(password)