def recur_fibo(g):
   if g <= 1:
       return g
   else:
       return(recur_fibo(g-1) + recur_fibo(g-2))
nterms = int(input("How many terms? "))
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
