#!/usr/bin/env python3


def isPalindrome(inputUser=None):
    if inputUser:

        inputUser_list = []
        for letter in inputUser:
            if letter != " ":
                inputUser_list.append(letter)

        reverse_inputUser_list = []
        for letter in inputUser:
            if letter != " ":
                reverse_inputUser_list.insert(0, letter)

        reverse_inputUser = "".join(reverse_inputUser_list)

        print(inputUser_list)
        print(reverse_inputUser_list)

        if inputUser_list == reverse_inputUser_list:
            return print(
                    f"It's a Palindrome. Your input {inputUser} " +
                    f"is equal to its reverse {reverse_inputUser}")
        else:
            return print("It isn't a Palindrome.")

    else:
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
            isPalindrome(inputUser)
            break


if __name__ == '__main__':
    main()
