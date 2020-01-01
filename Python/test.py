a=0
b=0
book=0
pencil=10
while(pencil==10):
   book=input("input unit\n")
   if book in('4'):
     que0=int(input("input score\n"))
     if (que0>=75 and que0<=100):
      score=12
      unit=3
      a=a+score
      b=b+unit
     elif(que0>=70 and que0<=74):
      score=10.5
      unit=3
      a=a+score
      b=b+unit
   if	book in('3'):
     que=int(input("input score\n"))
     if (que>=75 and que<=100):
      score=12
      unit=3
      a=a+score
      b=b+unit
     elif(que>=70 and que<=74):
      score=10.5
      unit=3
      a=a+score
      b=b+unit
     elif(que>=60 and que<=64):
      score=9
      unit=3
      a=a+score
      b=b+unit
     elif(que>=50 and que<=54):
      score=7.5
      unit=3
      a=a+score
      b=b+unit
   elif book in('2'):
      que2=float(input("input score\n"))
      if (que2>=75 and que2<=100):
        score=8
        unit=2
        a=a+score
        b=b+unit
      elif(que2>=70 and que2<=74):
        score=6.5
        unit=2
        a=a+score
        b=b+unit
      elif(que2>=55 and que2<=59):
        score=5.5
        unit=2
        a=a+score
        b=b+unit
   else:
       print("where you see 5 unit")
   try_again=input("do you want to try again? Continue or exit\n")
   if try_again in('y','yes','Y','YES'):
     pencil=10
   elif try_again in('n','no','N','NO'): 
     gp=a/b
     print("your gp is: ",gp)
     print("\n \n \n")
   elif try_again in('EXIT','exit'):
     exit()
   else:
     print("ARINDIN")
     pencil=exit()
   