 a = int(input("Enter lower range: "))
b = int(input("Enter upper range: "))

for num in range(a, b + 1):
   order = len(str(num))
    
   
   c = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       c += digit ** order
       temp //= 10

   if num == c:
       print(num)

