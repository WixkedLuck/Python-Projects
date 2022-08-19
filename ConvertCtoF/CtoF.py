#question one answer
def convertCtoF(number):
  CtoF=c*9/5+32
  c=int(number)
  
  print (String(c)+" degrees Celsius to farhenheit is: "+String(CtoF))

#question 2 answer
def oddOreven(number):
  c=int(number)
  d=c%2
  e=0
  if (d!=e):
     print ("the number is odd")
  else:
    print ("the number is even")
#question 3 answer
def threeinputs(num1,num2,num3):
  c=int(num1)
  d=int(num2)
  e=int(num3)
  if(c>d and c>e):
      print ("the greatest number is: "+String(c))
  elif(d>c and d>e):
      print ("the greatest number is: "+String(d))
  else :
    print(e)
#question four answer    
def CountoddOreven(word):
  c=String(word)
  temp=""
  tem=""
  for i in range(len(c)):
    if (i%2)==0:
      temp+=word[i]
    else: 
      tem+=word[i]
  print ("The word that was inputted is: "+c)
  print tem
  print temp
  
  
    
#question five answer

  
def count1(word):
  print (len(word)-word.count(' '))
   
 
  



def sam(num1,keyss):
  x=int(num1)
  L=String(keyss)
  s=0
  if (L=="C"):
    print ("converting to farheinght")
  else :
    print ("converting to c")



def buildCipher(key):
   
   if (letter in key=='C'):
      print ("Hi")