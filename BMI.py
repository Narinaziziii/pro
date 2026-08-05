

weight=float(input("inter your weight :"))
height=float(input("inter your height :"))

BMI=weight/((height*.01)**2)

if weight<0 or height<0:
    print("inter your numbers correctly")
elif BMI<18.5:
    print("underweight")
elif 18.5<=BMI<25:
    print("suitable weight")
elif 25<=BMI<30 :
    print("over weight")
elif BMI>30:
    print("FAT😣")
