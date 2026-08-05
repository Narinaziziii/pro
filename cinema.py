


age=float(input("sen khod ra vared konid:"))
day=str(input("rooz hafte ra vared konid:"))

if age<12:
    print(200*.5)
elif age>60:
    print(200*.3)

elif age<12 and day=='seshanbe':
    print(200*.5)
elif age>60 and day=='seshanbe':
    print(200*.3)

elif day=='seshanbe':
    print(200*.2)