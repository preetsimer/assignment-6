#question 1
def area(r):
    a=4*r*r*3.14
    print("The area of sphere is ",a)
n=int(input("Enter radius of sphere: "))
area(n)

#question 2
s=0
for num in range(1,1001):
    for i in range(1,num):
        if num%i==0:
            s=s+i
    if s==num:
        print(num)
    s=0    


#question 3
n=int(input("Enter a number: "))
print("The multiplication table of %d is:"%n)
for i in range(1,11):
    m=i*n
    print("%d * %d = %d"%(n,i,m))

#question 4
def power(a,b):
    if(b==1):
        return(a)
    if(b!=1):
        return(a*power(a,b-1))
a=int(input("Enter number: "))
b=int(input("Enter exponential value: "))
p=power(a,b)
print("%d^%d=%d"%(a,b,p))







    
