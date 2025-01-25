def call_namta(num, multiplier=1):
    # Base case: Stop recursion after 10 multiples
    if multiplier > 10:
        return
    # Print the current multiplication
    print(f"{num} x {multiplier} = {num * multiplier}")
    # Recursive call for the next multiplier
    call_namta(num, multiplier + 1)

# Input from the user
number = int(input("Enter a number to print its Namta: "))
call_namta(number)