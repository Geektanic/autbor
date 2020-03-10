# collatz-seq.py

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return(number // 2)
    else:
        print((3 * number) + 1)
        return((3 * number) + 1)

steps = 0

while True:
    try:
        user_number = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Please enter an integer.")
        continue

print("Your number will now be ran through the Collatz Sequence.")

if user_number == 1:
    print("1")
else:
    while user_number != 1:
        user_number = collatz(user_number)
        steps += 1

print(f"Collatz Sequence complete in {steps} steps.")