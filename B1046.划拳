#include <cstdio>

int main(){
	int n,x,a,y,b,failA = 0,failB = 0;
	scanf("%d",&n);
	while(n--){
		scanf("%d%d%d%d",&x,&a,&y,&b);
		if(a != b && a == x + y){
			failB++;
		}
		if(a != b && b == x + y){
			failA++;
		}
	}
	printf("%d %d",failA,failB);
	return 0;
}
