def Nsquared(n):
  #now make n squared
  n=n**2 
  print (n)

def sum(n):
  x=1
  y=0
  while(x<=n):
    y=y+x
    x=x+1
  print (y)
  
def acumgrade(mark1,mark2,mark3,mark4):
	x= mark1+mark2+mark3+mark4
	y=x/4
	if (y>=90):
		print "Score is A"
	elif (y>=80):
		print "Score is B"
	elif (y>=70):	
		print "Score is C"
	elif (y>=60):
		print "Score is D"
	else :
		print "Score is F"
