#include<stdio.h>
int main()
{
int i,j=0,l=0;
char a[50],b[25],c[25];
gets(a);
for(i=0;a[i]!='\0';i++)
{
if(i%2==0)
{
b[j]=a[i];
j++;
}
else
{
c[k]=a[i];
k++;
}
}
puts(b);
puts(c);
return 0;
}
