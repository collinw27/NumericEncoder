def decode_string(encoded_password):
    original_password = ""
    for digit in encoded_password:
        original_digit = str((int(digit) - 3) % 10)
        original_password += original_digit
    return original_password

def encode_string(string):
    output = ''
    for char in string:
        output += str((int(char) + 3) % 10)
    return output

def main():

    encoded_password = None

    while True:

        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        user_input = input("Please enter an option: ")

        if (user_input == "1"):
            encoded_password = encode_string(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
            print()
        elif (user_input == "2"):
            original_password = decode_string(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
            print()
        elif (user_input == "3"):
            break
        else:
            print("Invalid input. Please enter a number between 1 and 3.")
            print()

if (__name__ == '__main__'):
    main()
