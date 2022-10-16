def get_sum_of_multiples_of_3_and_5(limit):
    sum = 0
    number_list = []
    for number in range(0,limit):
        if number % 3 == 0 or number % 5 == 0:
            number_list.append(number)
    for number in number_list:
        sum += number
    return sum


print(get_sum_of_multiples_of_3_and_5(1000))
