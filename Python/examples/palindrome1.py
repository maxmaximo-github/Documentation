#!/usr/bin/env  python3


def isPalindrome(inputUser=None):
    if inputUser:
        reverse_inputUser = inputUser[::-1]
        if reverse_inputUser == inputUser:
            return print(
                    f"It's a Palindrome. Your input {inputUser} " +
                    f"is equal to its revers {reverse_inputUser}")
        else:
            return print("It isn't a Palindrome.")

    else:
        print(type(inputUser))
        return print("You don't input any value.")


def main():
    while True:
        inputUser = input("Enter your input: ")

        if inputUser.isnumeric():
            flag = input(
                    "Your input is not a string. Do you want continue? Y/N: ")
            if flag.lower() == "y":
                continue
            else:
                flag = None
                break
        else:
            print(type(inputUser))
            isPalindrome(inputUser)
            break


if __name__ == '__main__':
    main()
