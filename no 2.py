age=int(input("enter age"))
sex=input("enter sex")
marital=input("are you marrige")
if sex=="f":
    print("she will work only urban area")
if sex=="m":
    if age>=20 and age<=40:
        print("he work anywhere")
    elif age>=40 and age<=60:
        print("he work only urban area")
    else:
        print("none")
else:
    print("error")