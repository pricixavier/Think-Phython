#include<stdio.h>
void main()
{
    int m,r,sum=0;
    scanf("%d",&m);
    while(m!=0)
    {
        r=m%10;
        sum=sum+r*r;
        m=m/10;
    }
    printf("%d",sum);
}
