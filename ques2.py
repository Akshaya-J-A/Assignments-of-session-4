try:
    file1 = open("file.txt")
    print(file1.read())
except FileNotFoundError:
    print("File Not Found")



