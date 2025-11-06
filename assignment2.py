# 2.question 1:

def check_even_odd():
    try:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print(f"{num} is an even number.")
        else:
            print(f"{num} is an odd number.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    check_even_odd()



# 2.question 2:


def sum_numbers():
    total = 0
    for i in range(1, 51):
        total += i
    print(f"The sum of numbers from 1 to 50 is: {total}")

if __name__ == "__main__":
    sum_numbers()
