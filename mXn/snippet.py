import random
import sys
sum=0
m=input("enter the value of the row")
n=input("enter the value of the column ")
prod=m*n
while(sum!=prod):
    random_num=random.randrange(1,7)
    print"the value of the rolled die is",random_num
    if(sum+random_num<=prod):
     sum=sum+random_num
    x=sum%n
    y=sum/n
    
    if(y%2==1):
      x=n-1-x
    print "sum=",sum
    print"the position of the die is (x,y)=",y,x
    print"\n"

if(sum==prod):
    print "game won"

