print("Welcome to the Sawft Test \n")
print("please choose the correct option \n")
print("you also have 3 lifelines \n1)50/50 \n2)phone a friend \n3)Ask the audience \n")
print("you can only use a lifeline once and \n")
score=0
fifty=1
phone=1
audience=1
a=int(input("1.Proceed \n2.Exit \n"))
if (a==1):
    #while (a!=3108930000):
        Question_1=int(input("what is a rhesus \n1)A monkey \n2)a tiger \n3)a koala \n4) use a lifeline \n"))
        if (Question_1==1):
            print("correct")
            score+=1
        elif (Question_1==2):
            print("incorrect")
        elif (Question_1==3):
            print("incorrect")
        elif (Question_1==4):
           option=int(input("1)50/50 \n2)Phone \n3)audience \n"))
           if (option==1):
                ans=int(input(" The options are:- 1)monkey \n3)koala \n"))
                if (ans==1):
                    print("correct")
                    score+=1
                    fifty= fifty-1
                else:
                    print("wrong")
                
           elif (option==2):
                phone= int(input("Ringing..............\n The answer is 1):monkey \n"))
                if (phone==1):
                    print("correct")
                    score+=1
                else:
                    print("wrong")
           elif(option==3):
                audience= int(input("1.......30% \n2.........60% \n3.........10% \n"))
                if (audience==1):
                    print("correct")
                    score+=1
                else:
                    print("wrong")
           else:
                print("invalid option\n")
        else:
              print("invalid option")
             
print("your score is", score)
   
        
