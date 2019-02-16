#include<stdio.h>
int main()
{
int n,m=0,i,a[10];
m=a[0];
scanf("%d",&n);
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
for(i=0;i<n;i++)
{
if(a[i]<m)
m=a[i];
}
printf("%d",m);
return 0;
}
