def get_sum_of_fibonacci_numbers(limit):
    fibonacci_number = 0
    sum = 0
    number_list = [1,2]
    for number in range(1,limit):
     fibonacci_number = number_list[number] + number_list[number-1]
     number_list.append(fibonacci_number)
     if fibonacci_number > 4000000:
        break           
    for number in number_list:
        if number % 2 == 0:
            sum += number
    return sum


print(get_sum_of_fibonacci_numbers(1000))