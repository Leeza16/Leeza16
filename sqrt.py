import math


def check_squares(number):
    num = int(math.sqrt(number))
    for i in range(1, num + 1):
        first_num = pow(i, 2)
        second_num = number - first_num
        for j in range(1, num + 1):
            if pow(j, 2) == second_num:
                return True
    else:
        return False


number = 10
print(check_squares(number))
