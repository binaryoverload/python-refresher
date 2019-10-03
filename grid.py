def get_row_separator(columns, column_width):
    line = "+"
    for col in range(columns):
        line += "-" * column_width
        line += "+"
    return line

def get_row_line(columns, column_width):
    line = "|"
    for col in range(columns):
        line += " " * column_width
        line += "|"
    return line

def grid(columns=2, rows=2, column_width=4, row_height=4):
    grid = get_row_separator(columns, column_width) + "\n"
    for row in range(rows):
        for subRow in range(row_height):
            grid += get_row_line(columns, column_width) + "\n"
        grid += get_row_separator(columns, column_width) + "\n"
    return grid

if __name__ == "__main__":
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

    print(grid(columns, rows, column_width, row_height))