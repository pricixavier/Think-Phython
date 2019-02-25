#include<stdio.h>

int main(){
   int m,i,j,flag=1;
   scanf("%d",&m);
   for(i=2;i<=m;i++)
   {
       if(m%i==0)
       {
           flag=1;
           for(j=2;j<=i/2;j++)
           {
               if(i%j==0){
                flag=0;
                break;}
           }
           if(flag==1)
            {
                 printf("%d ",i);
            }
       }
        
    
   }
   return 0;
  
}
