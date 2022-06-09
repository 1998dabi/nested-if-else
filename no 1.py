day=input("enter the day")
mealtime=input("enter the mealtime")
if day=="monday":
    if mealtime=="breakfast":
        print("poori sabzi")
    elif mealtime=="lunch":
        print("sambhar rice")
    elif mealtime=="dinner":
        print("chiken rich")
    else:
        print("none")
elif day=="tuesday":
    if mealtime=="breacfast":
        print("poha")
    elif mealtime=="lunch":
        print("rajma rich")
    elif mealtime=="dinner":
        print("roti sabzi")
    else:
        print("not")
else:
    print("error")