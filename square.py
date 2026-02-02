def reverse_and_square(num):
    rev = int(str(num)[::-1])
    return rev, rev ** 2


# Take input from user
number = int(input("Enter a number: "))

# Function call
reversed_num, squared_value = reverse_and_square(number)

# Output
print("Reversed number:", reversed_num)
print("Square of reversed number:", squared_value)
