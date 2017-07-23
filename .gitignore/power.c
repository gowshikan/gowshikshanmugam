#include<stdio.h>
int main()
{
int base,exponent;
long long result=1;
print("enter a base number: ");
scanf("%d",&base);
printf("enter an exponent:");
scanf("%d",&exponent);
while(exponent!=0)
{
result*=base;
--exponent;
}
printf("answer=%11d",result);
return 0;
}
