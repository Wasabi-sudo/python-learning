temperature = 25
forecast = "Sun"
workday = True

if temperature > 80 and workday == False :
    print("Stay inside")
elif temperature < 60 and temperature >= 20 and forecast != "rainy":
    print("Enjoy! go out")
else:
    print("Go out!")