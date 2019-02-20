#include<stdio.h>
int main()
{
int i,j,k,count=0;
char m[100],n[100];
scanf("%[^\n]s",&m);
for(i=0;m[i]!='\0';i++)
{
count++;
}
j=0;
for(i=count-1;i>=0;i--)
{
n[j]=m[i];
j++;
}
for(i=0;i<count;i++)
{
printf("%c",b[i]);
}
}
