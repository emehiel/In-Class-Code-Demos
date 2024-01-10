# Error - no colon
#while True print('Hello world')

# Corrected
#while True: print('Hello world')

# or
#while True:
#    print('Hello world')

# No syntax Error
# x = 1 * (10/0)

try:
    #some code
    x = 1 * (10 / 0)
except ZeroDivisionError:
    # Executed if error in the
    # try block
    print("Can't divide by zero - the universe will explode")
else:
    # Execute is no exception
    print(f'The answer is {x}')
finally:
    # Some code - always executed
    print('Not mush to do here.')

# Raise an error in code
#try:
#    open('some data file.csv')
#except OSError:
#    raise RuntimeError('Unable to handle this error')

# define Python user-defined exceptions
class zerodivision(Exception):
	#Raised when the input value is zero
	pass
    # or you can do something to handle the error here

try:
	i_num = int(input("Enter a number: "))
	if i_num == 0:
		raise zerodivision
except zerodivision:
	print("Input value is zero, try again!")
	print()
