#include<stdio.h>
int main()
{
int a[50],i,m,large,small;
scanf("%d",&m);
for(i=0;i<m;++i)
scanf("%d",&a[i]);
large=small=a[0];
for(i=1;i<m;++i)
{
if(a[i]>large)
large=a[i];
if(a[i]<small)
small=a[i];
}
printf("%d",small);
printf("%d\t",large);
return 0;
}
