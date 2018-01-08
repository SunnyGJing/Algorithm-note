#include <cstdio>
int main(){
	int n,m,count=0;
	double a[1010] = {0}, x;
	scanf("%d",&n);
	while(n--){
		scanf("%d%lf",&m,&x);
		a[m] = x;
	}
	scanf("%d",&n);
	while(n--){
		scanf("%d%lf",&m,&x);
		a[m] += x;
	}
	for(int i=0; i<5; i++){
		if(a[i]!=0) count++;
	}
	printf("%d",count);
	for(int i=1010-1; i>=0; i--){
		if(a[i] != 0)  printf(" %d %.1lf",i,a[i]);
	}
	return 0;
}
