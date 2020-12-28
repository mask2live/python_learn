def weather(tempera):
    if tempera > 28:
        return "Hot"
    if tempera < 18:
        return "Cold"
    else:
        return "Warm"


if __name__ == "__main__" :
    temp = float(input("Enter a number of temperature: "))

    adject = weather(temp)

    print(adject)