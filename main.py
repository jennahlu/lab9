#Jenna Lu

def encode(password):
    encoded_password = ""
    for char in password:
        encoded_password += str((int(char) + 3) % 10)
    return encoded_password

def decode(encoded_password):
    pass

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input('''
Please enter an option: ''')

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print('''Your password has been encoded and stored!
                  ''')
        elif option == "2":
            original_password = decode(encoded_password)
            print(f'''The encoded password is {encoded_password}, and the original password is {original_password}.
                  ''')
        elif option == "3":
            break

if __name__ == "__main__":
    main()


