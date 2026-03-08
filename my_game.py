'''
1. create a program capable of displaying question to the user like kbc.
2. use list data type to store the questions and their correct answer.
3. display the final amount hte person is taking home after playing the game.
REMAINDER YOU CAN MAKE AS BIG AS YOU CAN BUT IM NOT DOIN IT TOO BIG.
'''
name = str(input("enter your name : "))

dob_day = int(input("enter birth date : "))
if(dob_day<0):
    print("invalid data")
elif(dob_day<=31):
    print("ok")
    dob_month = int(input("enter month : "))
    if(dob_month<0):
        print("invalid data")
    elif(dob_month>0 and dob_month<12):
        print("okay")
        dob_year = int(input("enter year : "))
        if(dob_year<1946):
            print("invalid data")
        elif(dob_year>=1946 and dob_year<2008):
            print("okay here is your question")
            first_question = ['what is the national bird of india?']
            print(first_question)
            print("1-peigon")
            print("2-parrot")
            print("3-peacock")
            print("4-woodpeaker")
            print("these are your options")
            x = int(input("would like to ans? (yes = 1/no = 0) : "))
            if(x==1):
                
                y = int(input("enter your option : "))
                if(y==1):
                    print("you loose")
                elif(y==2):
                    print("you loose")
                elif(y==4):
                    print("you loose")
                elif(y==3):
                    print("you win 10K Inr")
                else:
                    print("invalid input")
            elif(x==0):
                lifeline = int(input(("You won nothing. would you like to use lifeline??(yes=1/no=0) : ")))
                if(lifeline==1):
                    print("ok you've got 4 options!! ")
                    print("1 - 50-50")
                    print("2 - phone a friend.")
                    print("3 - ask an expert.")
                    print("4 - audience poll")
                    which_lifeline = int(input("enter your lifeline option : "))

                    if(which_lifeline==1):
                        print("your options are!")
                        print("2 - parrot")
                        print("3 - peacock")
                        Input2 = int(input("now what's your answer : "))
                        if(Input2==2):
                            print("you loose")
                        elif(Input2==3):
                            print("you win 10000inr")

                    elif(which_lifeline==2):
                        friends_num = int(input(("enter your friend's numeber : ")))
                        print("calling...",friends_num)
                        print("as your friend suggested you")
                        Input3 = int(input("what's your answer : "))
                        if(Input3==1):
                            print("you loose :( ")
                        elif(Input3==2):
                            print("you loose :( ")
                        elif(Input3==3):
                            print("you win 10000inr")
                        elif(Input3==4):
                            print("you loose :( ")
                        else:
                            print("invalid data")

                    elif(which_lifeline==3):
                        print("calling your expert...")
                        Input4 = int(input("as your expert suggested you which option will you choose : "))
                        if(Input4==1):
                            print("you loose :( ")
                        elif(Input4==2):
                            print("you loose :( ")
                        elif(Input4==3):
                            print("you win 10K inr")
                        elif(Input4==4):
                            print("you loose :( ")
                        else:
                            print("invalid data")
                    else:
                        print("invalid data")
                else:
                    print("invalid data")
            else:
                print("invalid data")
        else:
            print("invalid data")
    else:
        print("invalid data")      
else:
    print("invalid data")