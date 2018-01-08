#include <cstdio>
int main(){
	int a[1000]={0};
	int n,temp,m=0,num=0;
	while(scanf("%d%d",&temp,&n)!=EOF){
		a[n]=temp;
		m++;
	}
	for(int i=0; i<m; i++){
		if(a[i+1]!=0){
			a[i]=a[i+1]*(i+1);
			num++;
		}
		else
			a[i]=0;
	}
	a[m]=0;
	if(num==0) printf("%d %d",0,0);
	else{
		for( ; m >= 0;m--){
		if(a[m]!=0){
			printf("%d %d",a[m],m);
			num --;
			if(num!=0)
			printf(" ");
			}
		}
	}
	return 0;
}
