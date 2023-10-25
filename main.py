from decode import decode
from encode import encode

def main():
    encoded_password = None

    while True:
        selection = int(input(
            """Menu
------------
1. Encode
2. Decode
3. Quit
        
Please enter an option: """))

        if selection == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print(f"Your password has been encoded and stored!\n")

        if selection == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")

        if selection == 3:
            exit()


if __name__ == "__main__":
    main()
