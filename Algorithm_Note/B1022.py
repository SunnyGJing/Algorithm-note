#include <cstdio>  //已在pat通过 18-01-12 20:29
const int maxn=31;
int main(){
	int a, b, p;
	scanf("%d%d%d",&a,&b,&p);
	int x = a + b;
	int ans[maxn], i = 0;
	do{  // 进制转换 
		ans[i++] = x % p;
		x /= p;
	}while(x);
	for(int j= i-1; j>=0; j--){ //结果数输出 
		printf("%d",ans[j]);
	}
	return 0;
} 
