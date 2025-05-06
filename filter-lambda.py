number = range(1,101)

odd_numbers = filter(lambda n : n % 2 == 1 , number)
print(odd_numbers)
print(list(odd_numbers))