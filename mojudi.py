
mojudi=float(input("mojudi shoma cheghadr ast?"))
bardasht=float(input("meqdar bardasht cheghadr ast?"))


if bardasht<=0:
    print("mojudi bayad bishtr az 0 bashd")
elif bardasht>mojudi :
    print("boro kar kon zooret nemirse")

elif mojudi-bardasht<=100:
    print(mojudi-bardasht,'❌hoshdarrr')
else:
    print(mojudi-bardasht)