import random

def generate_random_float(start, end):
    random_float = random.uniform(start, end)
    return random_float

def main():
    start = float(input("Enter the start of the range: "))
    end = float(input("Enter the end of the range: "))

    
    random_float = generate_random_float(start, end)
    print("Random floating-point number:", random_float)

if __name__ == "__main__":
    main()
