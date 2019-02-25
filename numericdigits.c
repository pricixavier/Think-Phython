#include<stdio.h>
int main(void)
{
int m,n1,count=0;
scanf("%d",&m);
while(m!=0)
{
n1=m%10;
count++;
m=m/10;
}
printf("%d",count);
}
