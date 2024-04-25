a=[1,2,3,4]
try:
    i=int(input("Enter the index:"))
    print(a[i])
except IndexError:
    print("Please enter valid index")
    