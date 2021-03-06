#include <cstdio>
int main(){
	int n, i;
	char ch;
	scanf("%d",&n);
	getchar();
	ch = getchar();   //输入完成
	n -= 1;
	for(i = 2; n >= 2*(2*i-1);i++)
		n -= 2*(2*i-1); //循环结束时，i-1=行数（上倒三角），n=剩余个数
	int r = i-1; //处理结束，下面开始打印输出
	// 输出上面的倒三角形
	for(int j=r; j>0; j--){
		for(int q=j; q<r; q++) printf(" "); //打印空格
		for(int k=0;k<(2*j)-1;k++)
			printf("%c",ch); //打印某一行的符号 
		printf("\n"); 
	}
	// 输出下面的正三角形（去尖）
	for(int j=2; j<=r; j++){
		for(int q=(((2*r)-1)-((2*j)-1))/2; q>0; q--) printf(" "); 
		for(int k=0;k<(2*j)-1;k++)
			printf("%c",ch); //打印某一行的符号 
		printf("\n"); 
	}        
	// 输出剩余个数
	printf("%d",n); 
	return 0;
} 
