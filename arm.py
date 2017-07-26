
x= int(input("Enter a number: "))

y = 0

t = x
while t > 0:
   digit = t % 10
   y += digit ** 3
   t //= 10

if x==y:
   print(x,"is an Armstrong number")
else:
   print(x,"is not an Armstrong number")
