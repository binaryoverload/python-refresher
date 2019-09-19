columns = int(input("How many columns?"))
column_width = int(input("What is the width of the columns?"))
if column_width < 1:
    print("Column width needs to be at least 1!")
    exit(1)

rows = int(input("How many rows?"))
row_height = int(input("What is the height of the rows?"))
if row_height < 1:
    print("Row height needs to be at least 1!")
    exit(1)


def get_row_separator():
    line = "+"
    for col in range(columns):
        line += "-" * column_width
        line += "+"
    return line

def get_row_line():
    line = "|"
    for col in range(columns):
        line += " " * column_width
        line += "|"
    return line

def get_row():
    row = ""
    for subRow in range(row_height):
        row += get_row_line()
        # Don't add a newline onto the last row
        if subRow < row_height - 1:
            row += "\n"
    return row


print(get_row_separator())
for row in range(rows):
    print(get_row())
    print(get_row_separator())
