
try:
    with open('plaintext.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")
