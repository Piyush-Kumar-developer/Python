temp = int(input("Enter the Temperature:"))
if temp < 0:
    print("Freezing")
elif temp <= 0 and temp < 20:
    print("Cold")
elif temp >= 21 and temp <35:
    print("Warm")
else:
    print("Hot")