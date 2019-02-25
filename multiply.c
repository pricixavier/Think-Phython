
#include <stdio.h>

int main()
{
   int m,n,i;
   printf("enter m and n");
   scanf("%d%d",&m,&n);

   for(i=1;;i++)
   {
       if(((i%m)==0)&&((i%n)==0))
       {
           printf(" %d",i);
           break;
       }
   }
   
    return 0;
}
