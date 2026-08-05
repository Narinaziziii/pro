

age=int(input("how old are you?:"))

if age<=18 :
    print("bye bye")

else:
    username=str(input("inter username:"))
    password=str(input("inter password:")) 

    if username=='dark_shadow'and password=='king arthur 7300':
         print("login done")

    elif username!='dark_shadow' and password=='king arthur7300':
         print("wrong username")

    elif password!='king arthur 7300'and username=='dark_shadow':
         print("password wrong")

    else:
         print("password and username are wrong")