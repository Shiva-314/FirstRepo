# print("Hello Shiva Sir !")

# U = int(input("Enter num1: "))
# U2 = int(input("Enter num2: "))


U = int(input("Enter Sq to get Squrt: "))
for i in range(2, U):
    if (U%i == 0 and U // i == i):
        print(f"Hence the Sqrt of {U} is: {i}")