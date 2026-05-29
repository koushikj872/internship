password = "Secret"
i = 1

while i <= 5:
    p = input("Enter the password: ")

    if p == password:
        print("Congrats! Access Granted")
        break
    else:
        print(f"Wrong Password! You have {5 - i} more attempts")

    i += 1

if i > 5:
    print("Too many failed attempts. Access Denied.")
