import random

def generate_and_save_random_number(filename):
   
    random_number = random.randint(1, 100)  

    
    with open(filename, "w") as file:
        file.write(str(random_number))

    print(f"Random number {random_number} saved to '{filename}'.")

def main():
    filename = "random_numbers.txt"
    generate_and_save_random_number(filename)

if __name__ == "__main__":
    main()
