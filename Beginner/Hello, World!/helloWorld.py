# defining a function without taking in any variables
def main():
    # Use print() function to display messages in terminal
    print("Hello, World")

def harder():
    # input() will allow the user to enter any data, and apply it to a variable "name"
    name = input("What is your name?\n") # Note that '\n' will start a new line, like hitting enter in a text file

    # Here are two methods to print strings with variables
    print(f"Hello, {name}!")
    print("Nice to meet you, {}!".format(name))

# calling functions to actually be run
main()
harder()
