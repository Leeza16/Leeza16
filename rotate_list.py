def rotate_list(input_list, n):
    output_list = [0] * len(input_list)
    num_right = len(input_list) - n
    num_left = len(input_list) - num_right
    for i in range(0, num_right):
        output_list[i+n] = input_list[i]

    for i in range(0, num_left):
        output_list[i] = input_list[i + num_right]

    return output_list


input_list = [1, 2, 3, 4, 5, 6, 7, 8]
output_list = rotate_list(input_list, 2)
print(output_list)
