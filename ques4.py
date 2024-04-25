def new_file():
    file="new_file.txt"
    with open(new_file, 'w') as file:
        file.write("Hello, this is a new text file created using open() function.")
    print(f"File '{new_file}' created successfully.")
new_file()