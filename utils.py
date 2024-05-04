# Creating a class named Utils
class Utils:
    # Function that reverses the number
    def Reversed(number):
        # Converting the number to string
        numAsStr = str(number)

        # Two scenarios when number is a single digit vs. greater digits
        if number < 10:
            print("The reverse of the number " + numAsStr + " is " + numAsStr + "0.")
        else:
            reversedNumber = numAsStr[::-1]
            print("The reverse of the number " + numAsStr + " is " + reversedNumber + ".")

    # Function that converts decimal number into binary and octal
    def Formatter(number):
        print("The value of " + str(number) + " is:")
        print(str(bin(number)) + " in binary.")
        print(str(oct(number)) + " in octal.")