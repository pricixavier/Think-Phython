#include<stdio.h>
int main(void){
	int m;
	scanf("%d",&m);
	if(m!=0){
	while(m!=0){
		printf("%d",(m%10));
		m=m/10;
	}
	}
	else{
		printf("0");
	}
}
