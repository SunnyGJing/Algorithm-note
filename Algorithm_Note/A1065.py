// 未实现！！！！！

#include <cstdio>
int main(){
	int n, ans;
	long long a,b,c;
	scanf("%d",&n);
	for(int i=0; i<n; i++){
		scanf("%lld%lld%lld",&a,&b,&c);
		if((c-a) < b)
			printf("Case #%d:true",i+1);
		else
			printf("Case #%d:false",i+1);
	}
}
