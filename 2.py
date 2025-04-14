my_list=[123]

#write code to separate the elements of the list by comma

# Separate the digits of the integer into a list
result = [int(digit) for digit in str(my_list[0])]

print(result)  # Output: [1, 2, 3]