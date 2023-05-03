import re

def main():
    print("Hello, I am Eliza. How can I help you?")
    while True:
        user_input = input(">> ")
        if user_input == "Bye":
            print("See you later...")
            break
        elif re.search(r'\b(Where am I)\b', user_input):
            print("Next to me.")
        elif re.search(r'\b(How did I come here|What brought me here|What am I doing here)\b', user_input):
            print("You have been selected by the Matrix.")
        elif re.search(r'\b(Who is the matrix|Who is this Matrix you talking about|What are you talking about)\b', user_input):
            print("It is the future.")
        else:
            print("Things will become clearer soon.")

if __name__ == "__main__":
    main()