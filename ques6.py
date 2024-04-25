def count_words(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()
            word_count = len(text.split())
            print(f"Total number of words in '{filename}': {word_count}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
count_words("poem.txt")
