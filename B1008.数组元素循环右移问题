#if(0)
#include <cstdio>
int main(){
	int n,m,A[100],i,j,k,p=1,temp;
	scanf("%d%d",&n,&m);
	for(int i=0; i<n; i++){
		scanf("%d",&A[i]);
	}
	j = n;
	k = m;
	while(k--){
		i = n - 1;
		temp = A[j-1];
		while(--i){
			if(i%m == 0)
				A[i+m-p] = A[i-p];
		}
		A[k] = temp;
		j--;
		p++;
	}
	for(i=0; i<n; i++){
		printf("%d ",A[i]);
	}
	return 0;
}
#endif

#if(0)
#include <cstdio>
int main(){
	int A[110];
	int n, m;
	scanf("%d%d",&n, &m);
	m = m % n;           //修正m
	for(int i=0; i<n; i++){
		scanf("%d",&A[i]);
	}
	int i = m;
	while(i--){
		printf("%d ",A[n-i-1]);
	}
	for(int i=0; i<n-m; i++){
		printf("%d",A[i]);
		if(i<n-m-1) printf(" ");
	}
	return 0;
}
#endif

#if(1)
#include <cstdio>
int main(){
	int a[110];
	int n, m, count;
	scanf("%d%d",&n, &m);
	m = m % n;           //修正m
	for(int i=0; i<n; i++){
		scanf("%d",&a[i]);
	}
	for(int i = n - m; i < n; i++){
		printf("%d", a[i]);
		count++;
		if(count < n) printf(" ");      //当输出数的个数小于n，则输出空格 
	}
	for(int i = 0; i < n - m; i++){
		printf("%d",a[i]);
		count++;
		if(count < n) printf(" ");
	}
	return 0;
}
#endif
