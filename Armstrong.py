
num = int(input("Enter a number: "))

sum = 0


a = num
while a > 0:
   digit = a % 10
   sum += digit ** 3
   a //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")