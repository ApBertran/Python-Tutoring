def main():
    # Take in values for x and y; using int() will guarentee that the number is stored as an integer
    x = int(input("Input first value: \n"))
    y = int(input("Input second value: \n"))

    # Using print(f""") we can print variables
    print(f"{x} + {y} = {x + y}\n")
    print(f"{x} - {y} = {x - y}\n")
    print(f"{x} * {y} = {x * y}\n")
    print(f"{x} / {y} = {(x / y):.2f}\n") # Note the use of () and :.2f
    # ':.2f' turns the float created from x/y into a number only displaying 2 decimal points
    print(f"{x} % {y} = {x % y}\n")

main()
