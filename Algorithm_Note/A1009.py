// 做对了~  但有待改进哦！（看书！） 

#include <cstdio>
const int maxn = 1010;
int main(){
	int n, e, count=0;
	double k, a[maxn]={0}, b[maxn]={0}, c[2*maxn]={0}; 
	scanf("%d",&n);
	for(int i=0; i<n; i++){
		scanf("%d%lf",&e,&k);
		a[e] = k;
	}
	scanf("%d",&n);
	for(int i=0; i<n; i++){
		scanf("%d%lf",&e,&k);
		b[e] = k;
	}
	for(int i=0; i<maxn; i++){
		for(int j=0; j<maxn; j++){
			c[i+j] += a[i] * b[j];
		}
	}
	for(int i=0; i<maxn; i++){
		if(c[i]!=0.0) count++;
	}
	printf("%d",count);
	for(int i=maxn-1; i>=0; i--){
		if(c[i]!=0.0) printf(" %d %.1lf",i,c[i]);
	}
	return 0;
}
