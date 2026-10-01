


'''while True :
    list_score=[]
    while True:
        lessons=input("1.scores 2.ave 3.exit : ")
        match lessons:
            case "1":
                math=float(input("math score :"))
                list_score.append(math)
                biology=float(input("biology score:"))
                list_score.append(biology)
                chemistry=float(input("chemistry score:"))
                list_score.append(chemistry)
               
                jam=sum(list_score)
                miu=jam/3
                print(list_score)
                print(miu)'''



while True:
   import random 
   

   list_person=[]

   while True:
      person1=input("nam aval ra vared konid: ")
      person2=input("nam dovom ra vared konid:")
      person3=input("nam sevon ra vared konid:")
      person4=input("nam charom ra vared konid:")


      list_person.append(person1)
      list_person.append(person2)
      list_person.append(person3)
      list_person.append(person4)


      print(random.choice(list_person))
      