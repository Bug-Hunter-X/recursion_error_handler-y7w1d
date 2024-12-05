def my_function(x):
    if x < 0:
        return 0  # Handle negative input
    elif x == 0:
        return 0
    else:
        return my_function(x - 1) + 1

print(my_function(5))  # Output: 5
print(my_function(0))  # Output: 0
print(my_function(-1)) # Output: 0