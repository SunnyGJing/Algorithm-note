#include <cstdio>  //已在pat通过  18年1月14日 14:14
int main(){
	bool flag = true;
	int x, y;
	scanf("%d %d",&x,&y);
	int sum = x + y;
	if(sum<0){
		flag = false;
		sum = -sum;
	}
	int num=1, a[10];
	do{
		a[num++]=sum%10;
		sum /= 10;
	}while(sum);
	char b[15];
	int i=0;
	for(int j=1; j<= num-1; j++){
		b[i++] = a[j]+'0';
		if(j%3==0&&j!=num-1) b[i++]=',';
	}
	if(flag==false) printf("-");
	for(int k=i-1; k>=0; k--){
		printf("%c",b[k]);
	}
	return 0;
}
