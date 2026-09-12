

print("welcome ")
print("nila cafe")

while True :
    menu=input("1.cafe 2.brunch 3.drinks 4.food 5.boardgame 6.exit:")
    while True :
        match menu :
            case "1":
                cafe_menu=input("1.late 2.caramel late 3.frape 4.exit:")
                match cafe_menu :
                    case"1":
                        num_late=int(input("num of order:"))
                        price_late=num_late*300*1.1
                        print("late price....",price_late)
                    case"2":
                        num_caramel=int(input("num of order:"))
                        price_caramel=num_caramel*380*1.1
                        print("caramel price....",price_caramel)
                    case"3":
                        num_frape=int(input("num of order:"))
                        price_frape=num_frape*450*1.1
                        print("frape price....",price_frape)
                break 
            case "2" :
                brunch_menu=input("1.bacon 2.avocado toast 3.omelette 4.french toast 5.exit:") 

                match brunch_menu:
                    case "1":
                        num_bacon=int(input("num of order:"))   
                        price_bacon=num_bacon*890*1.1
                        print("price bacon....",price_bacon) 
                    case "2" :
                        num_avocado_toast=int(input("num of order:"))
                        price_avocado=num_avocado_toast*900*1.1
                        print("price avocado toast ",price_avocado)
                    case "3" :
                        num_omelette=int(input("num of order:"))
                        price_omelette=num_omelette*780*1.1
                        print("price omelette ....",price_omelette)
                    case "4" :
                        num_french=int(input("num of order:"))
                        price_french=num_french*700*1.1
                        print("price french toast....",price_french)
                break
            case "3":
                drinks_menu=input("1.mojito 2.pink lady 3.strawberry matcha 4.breeze 5.exit")
                match drinks_menu:
                    case "1":
                        num_mojito=int(input("num of order:"))
                        price_mojito=num_mojito*300*1.1
                        print("price mojito....",price_mojito)
                    case "2":
                        num_pink_lady=int(input("num of order:"))
                        price_pink=num_pink_lady*450*1.1
                        print("price pink lady....",price_pink)
                    case "3":
                        num_strawberry=int(input("num of order:"))
                        price_strawberry=num_strawberry*600*1.1
                        print("price strawberry mmatcha....",price_strawberry)
                    case "4":
                        num_breeze=int(input("num of order:"))
                        price_breeze=num_breeze*900*1.1
                        print("price breeze :) ....",price_breeze)
                break
            case "4":
                food_menu=input("persian or fastfood ?")
                if food_menu=="persian":
                    persian=input("1.kabab 2.zereshk polo 3.qeyme 4.exit")
                    match persian:
                        case "1":
                            num_kabab=int(input("num of order:"))
                            price_kabab=num_kabab*1200*1.1
                            print("price kabab....",price_kabab)
                        case "2":
                            num_zereshk=int(input("num of order:"))
                            price_zereshk=num_zereshk*1500*1.1
                            print("price zereshk polo....",price_zereshk)
                        case "3":
                            num_qyme=int(input("num of order:"))
                            price_qeyme=num_qyme*990*1.1
                            print("price qeyme ....",price_qeyme)
                    break
                if food_menu=="fastfood" or food_menu==" fast food":
                    fastfood=input("1.sandwich 2.burger 3.pizza 4.exit")
                    match fastfood:
                        case "1":
                            num_sandwitch=int(input("num of order:"))
                            price_sandwich=num_sandwitch*780*1.1
                            print("price sandwitch....",price_sandwich)
                        case "2":
                            num_burger=int(input("num of order:"))
                            price_burger=num_burger*880*1.1
                            print("price burger",price_burger)
                        case "3":
                            num_pizza=int(input("num of order:"))
                            price_pizza=num_pizza*1000*1.1
                            print("price pizza ....",price_pizza)
                    break
                break
            case "5":
                print("coming soon :) ")
        break

    break
           
                    
                    
        

                
                
            
