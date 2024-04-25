def read_poem():
    try:
        with open("poem.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Error: File 'poem.txt' not found.")
read_poem()
