#include <cstdio>
const int maxn = 210; 
int main(){
	int a[maxn];
	int n, ans = -1, x;
	while(scanf("%d",&n)!=EOF){
		for(int i=0; i < n; i++){
			scanf("%d",&a[i]);
		}
		scanf("%d",&x);
		for(int j=0; j < n; j++){
			if(a[j] == x) ans = j;
		}
		printf("%d",ans);
	}
	return 0;
}
