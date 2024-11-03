list = [455, 26, 4, 62, 71, 57, 13]

# len(list)

item = int(input("Enter a Number: "))

for i in range (len(list)):
    if list[i] == item:
        print("Found at Index", i)
        break
else:
        print("Not Found")