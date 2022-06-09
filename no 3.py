expeted_day=int(input("enter expeted_day"))
expeted_month=int(input("enter expeted_month"))
expeted_year=int(input("enter expeted_year"))
return_day=int(input("enter return_day"))
return_month=int(input("enter return_month"))
return_year=int(input("enter return_year"))
if expeted_month==return_month and expeted_year==return_year:
    if return_day<=expeted_day:
        print("no fine")
    elif return_day>=expeted_day:
        number_day_late=return_day-expeted_day
        fine=15*number_day_late
        print("number_day_late=",number_day_late)
        print("fine",fine)
    else:
        print("not")
elif return_day>=expeted_day and return_year==expeted_year:
    if return_month>=expeted_month:
        number_day_late=return_day-expeted_day
        number_month_late=(return_month-expeted_month)*30
        number_late=number_month_late-number_day_late
        fine=500*number_late
        print("number_month_late=",number_late)
        print("fine=",fine)
    else:
        print("fine charged")
elif return_month==expeted_month and return_day==expeted_day:
    if return_year>=expeted_year:
        fixed_fine=10000
        print("fine=",fixed_fine)
    else:
        print("none")
else:
    print("no fixed_fine")

    