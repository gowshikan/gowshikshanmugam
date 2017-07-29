def computeHCF(a, b):
    if a > b:
        smaller = b
    else:
        smaller = b
    for i in range(1, smaller+1):
        if((a % i == 0) and (b % i == 0)):
            hcf = i
            
    return hcf

num1 = 54 
num2 = 24
print("The H.C.F. of", num1,"and", num2,"is", computeHCF(num1, num2))
