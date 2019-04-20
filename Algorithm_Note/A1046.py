#include <cstdio>
const int maxn = 100010;
int d[maxn];
int main(){
	int n,m,x,y,d1,d2;
	scanf("%d",&n);
	for(int i=0; i<n; i++){
		scanf("%d",&d[i]);
	}
	scanf("%d",&m);
	int shortest[m];
	for(int i=0; i<m; i++){
		scanf("%d%d",&x,&y);
		d1 = d2 = 0;
		for(int j=x; j%(n+1)!=y; j++){
			d1 += d[j%(n+1)-1];
		}
		for(int k=y; k%(n+1)!=x;k++){
			d2 += d[k%(n+1)-1];
		}
		shortest[i] = d1;
		if(shortest[i] > d2) shortest[i] = d2;
	}
	for(int i=0; i<m; i++){
		printf("%d\n",shortest[i]);
	}
} 
