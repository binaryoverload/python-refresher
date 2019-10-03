def caesar_cipher(str, shiftBy):
    output = ""
    for char in str.lower():
        if char == ' ':
            output += ' '
            continue
        output += chr(97 + (((ord(char) - 97) + shiftBy) % 26))

    return output

if __name__ == "__main__":
    strInput = input("Enter string to shift: ")
    shift = int(input("Enter number of places to shift by: "))

    print(caesar_cipher(strInput, shift))