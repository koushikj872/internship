def play_outside(outlook, humidity, windy):

    if outlook.lower() == "overcast":
        return "Yes"

    elif outlook.lower() == "sunny":
        if humidity.lower() == "high":
            return "No"
        else:
            return "Yes"

    elif outlook.lower() == "rain":
        if windy.lower() == "yes":
            return "No"
        else:
            return "Yes"

# User Input
outlook = input("Enter Outlook (Sunny/Overcast/Rain): ")
humidity = input("Enter Humidity (High/Normal): ")
windy = input("Is it Windy? (Yes/No): ")

print("Play Outside:", play_outside(outlook, humidity, windy))