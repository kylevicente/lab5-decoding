# Function to convert decimal to ASCII manually
def decimal_to_ascii(num):

    # Numbers 0-9
    numbers = ["0","1","2","3","4","5","6","7","8","9"]

    # Uppercase letters
    uppercase = [
        "A","B","C","D","E","F","G","H","I","J","K","L","M",
        "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
    ]

    # Lowercase letters
    lowercase = [
        "a","b","c","d","e","f","g","h","i","j","k","l","m",
        "n","o","p","q","r","s","t","u","v","w","x","y","z"
    ]

    if 48 <= num <= 57:
        return numbers[num - 48]

    elif 65 <= num <= 90:
        return uppercase[num - 65]

    elif 97 <= num <= 122:
        return lowercase[num - 97]

    elif num == 32:
        return " "

    elif num == 44:
        return ","

    elif num == 45:
        return "-"

    elif num == 46:
        return "."

    else:
        return ""

repeat = 1
while repeat == 1 or repeat =="Y":
# Ask for file name
    filename = input("Enter file name: ")
    filename = "Activity 5 - Decoding/" + filename + ".txt"

    # Open the file
    file = open(filename, "r")

    binary_text = file.read()

    file.close()

    # Remove spaces and newlines
    binary_text = binary_text.replace(" ", "")
    binary_text = binary_text.replace("\n", "")

    decoded_message = ""

    index = 0

    # Read binary 8 bits at a time
    while index < len(binary_text):

        byte = binary_text[index:index+8]

        if len(byte) == 8:

            decimal_value = int(byte, 2)

            character = decimal_to_ascii(decimal_value)

            decoded_message = decoded_message + character

        index = index + 8

    print("\nBinary Text:")
    print(f"{binary_text}\n")
    print("\nDecoded Message:")
    print(decoded_message)

    repeat = input("Do you want to repeat the program?[Y/N]: ").upper()
    while repeat != "Y" and repeat != "N":
        print("wrong input!")
        repeat = input("Do you want to repeat the program?[Y/N]: ").upper()
    if repeat != "Y":
        break


    