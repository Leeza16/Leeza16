def check_numbers(num1, num2):
    num_list = set()
    for i in range(num1 + 1, num2 + 1):
        for j in range(num1, i + 1):
            if j == i:
                pass
            elif i % j == 0:
                num_list.add(i)
    return [num_list, len(num_list)]


num1 = 100
num2 = 100
print(check_numbers(num1, num2))
