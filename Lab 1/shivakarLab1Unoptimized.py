from time import process_time

t1_start = process_time()

# Initialization
factorial = 1
# Setting range between 1 to 100
x = range(1, 101)
# Loops 1 through 100
for n in x:
    # Setting range between 1 to whatever value of n is being looped
    y = range (1, n + 1)
    # Looping through defined y range for factorial multiplication
    for m in y:
        # Multiplying factorial incremented by 1 till the number of which the factorial is being calculated
        factorial = factorial*m
    # Printing value to terminal
    print(factorial)
    # Setting factorial value back to 1 for next number's calculation
    factorial = 1

t1_stop = process_time()
print(t1_stop - t1_start)