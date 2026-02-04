a = int(input("Enter the first side of triangle: "))
b = int(input("Enter the second side of triangle: "))
c = int(input("Enter the third side of triangle: "))
if (a + b) > c and (b + c) > a and (c + a) > b:
    print("Triangle is valid")
else:
    print("Triangle is not valid")