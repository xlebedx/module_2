my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_list_beginning_index = 0
while my_list[my_list_beginning_index] >= len(my_list) and my_list[my_list_beginning_index] > 0:
    print(my_list[my_list_beginning_index])
    my_list_beginning_index += 1
    if my_list[my_list_beginning_index] == 0:
        my_list_beginning_index += 1
    if my_list[my_list_beginning_index] < 0:
        break