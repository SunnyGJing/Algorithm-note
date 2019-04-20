#include <cstdio>
int main(){
	int n, r;
	char ch;
	scanf("%d",&n);
	getchar();    //吃掉空格 
	ch = getchar();    //输入部分结束
	r = (n*10/2+5)/10; //求行数  处理部分结束 
	for(int i=0; i<n; i++) printf("%c",ch);
	printf("\n");
	for(int i=0; i<r-2; i++){
		printf("%c",ch);
		for(int j=0; j<n-2; j++)
			printf(" ");
		printf("%c\n",ch);
	}
	for(int i=0; i<n; i++) printf("%c",ch);
	return 0;
} 

/* 第8行 r = (n*10/2+5)/10; 的改进如下：
   题目说明行数是列数的50%（四舍五入）
   故当列数为偶数时，行数 = 列数/2；当列数为奇数时，行数 = 列数/2+1 */ 
