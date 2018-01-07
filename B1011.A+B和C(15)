#if(0)
#include <cstdio>
int main(){
	int n;
	scanf("%d", &n);
	while(n <= 0 || n > 10){
		scanf("%d", &n);
	}
	int a[n][3] = {0};
	for(int i = 1; i <= n; i++){
		scanf("%d%d%d", &a[i][0], &a[i][1], &a[i][2]);
	}
	for(int i = 1; i <= n; i++){
		if(a[i][0] + a[i][1] > a[i][2])
			printf("Case #%d:true\n",i);
		else
			printf("Case #%d:false\n",i);
	} 
	return 0;
}
#endif

#if(1)
#include <cstdio>
int main(){
	int T, tcase = 1;
	long long a, b, c;
	scanf("%d",&T);
	while(T--){
		scanf("%lld%lld%lld",&a,&b,&c);
		if(a + b > c)
			printf("Case #%d:true",tcase++);
		else
			printf("Case #%d:false",tcase++);
	}
	return 0;
} 
#endif
