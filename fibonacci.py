# Fibonacci sequence generator up to n numbers

def print_fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        print(a, end=' ')
        a, b = b, a + b
        count += 1
    print()  # for newline

if __name__ == "__main__":
    try:
        num = int(input("How many Fibonacci numbers do you want to print? "))
        if num <= 0:
            print("Please enter a positive integer.")
        else:
            print_fibonacci(num)
    except ValueError:
        print("Invalid input. Please enter an integer.")
