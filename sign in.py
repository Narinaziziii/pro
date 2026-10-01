

print("sign in form")
while True:
 list1=[]
 first_form=input("1.sign up 2.sign in :")
 while True:
  match first_form:
   case "1":
    first_name=input("inter your first name : ").capitalize()
    list1.append(first_name)
    last_name=input("inter your last name : ").capitalize().title()
    list1.append(last_name)
    while True:
         phone=(input("inter your phone number : "))
         if len(phone)==11 :
            list1.append(phone)
         else :
          print("phone number must be 11 digits ! ")
         break
    adress=input("inter your home adress : ")
    list1.append(adress)
    post_code=(input("inter your post code : "))
    list1.append(post_code) 

    gender= input("1.male 2.female 3.other : ")
    match gender:
      case "1":
        list1.append("male")
      case "2":
        list1.append("female")
      case "3":
        list1.append("other")
    username=input("inter your username:")
    list1.append(username)
    while True:

     password=input("inter your password :")
     if len(password)<8:
         print("password must be more than 8 digits!")
     else :
         list1.append(password)
     break
   case "2" :
      username1=input("inter username:")
      password1=input("inter password:")
      if username1==list1[6] and password1==list1[7] :
        print ("login")
      else:
        print("wrong")
        continue

  print(list1)

   
  

 