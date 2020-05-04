
# The collatz function

def collatz(number):
    if number%2 == 0:
        val = number // 2
        print(val)
        return val
    else:
        val = 3 * number + 1
        print(val)
        return val

# after input handling

print("Enter a number:")
try:
    num = int(input())
    val = collatz(num)
    while val != 1:
        val = collatz(val)
except ValueError:
    print("Please enter an integer")