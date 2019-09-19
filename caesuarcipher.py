strInput = input("Enter string to shift: ")
shift = int(input("Enter number of places to shift by: "))

strInput = strInput.lower()

output = ""
for char in strInput:
    output += chr(97 + (((ord(char) - 97) + shift) % 26))

print(output)