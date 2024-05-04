from time import process_time

t1_start = process_time()

# Initialization
factorial = 1
# Setting range between 1 to 100
x = range(1, 101)
# Loops 1 through 100
for n in x:
    # Multiplying previous factorial value with next value n
    factorial = factorial*n

    # Printing value to terminal
    print(factorial)


t1_stop = process_time()
print(t1_stop - t1_start)