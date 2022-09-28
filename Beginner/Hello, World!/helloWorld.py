# defining a function without taking in any variables
def main():
    # Use print() function to display messages in terminal
    print("Hello, World")

def harder():
    # input() will allow the user to enter any data, and apply it to a variable "name"
    name = input("What is your name?\n")

    # Here are two methods to print strings with variables
    print(f"Hello, {name}!")
    print("Nice to meet you, {}!".format(name))

# calling functions to actually be run
main()
harder()
