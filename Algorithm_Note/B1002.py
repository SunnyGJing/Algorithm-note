#include <cstdio>   // 已在pat通过  18年1月13日 17:09 
#include <cstring>
const char a[10][5]={"ling","yi","er","san","si","wu","liu","qi","ba","jiu"};
int main(){
	char str[110];
	gets(str);
	int len = strlen(str)；
	int sum=0;
	for(int i=0; i<len; i++)
		sum += str[i]-'0';
	int ans[4], num=0;
	do{
		ans[num++] = sum%10;
		sum /= 10; 
	}while(sum);
	for(int j=num-1; j>=0; j--){
		printf("%s",a[ans[j]]);
		if(j) printf(" ");
	}
	return 0;
}
 
