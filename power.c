#include <stdio.h>
int main(void) {
	int b,t,flag=0;
	scanf("%d",&b);
            t=b;
            
            
              if(t%2!=0)
              {
               flag=1;
              }
            
            if(flag==0)
            {
              printf("yes");
            }
            else
            {
              printf("no");
            }
	return 0;
	
}
