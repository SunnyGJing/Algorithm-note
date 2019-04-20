#include <cstdio>  //已在pat通过  18年1月13日 14:44	 
int main(){
	int x, n=1;
	scanf("%d",&x);
	int b= x/100;
	int s= x%100/10;
	int g= x%10;
	while(b--) printf("B");
	while(s--) printf("S");
	while(g--) printf("%d",n++);
	return 0; 
} 
