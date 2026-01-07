num=int(input("Enter the number whose sum you want to calculate: "))
sum=0
for i in range(1,num+1):
    sum=sum+i
print("Sum of first",num,"natural numbers is",sum)