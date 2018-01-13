#if(0)
#include <cstdio>   //已在pat通过  1月13日 13:37	
// 这个简洁方法只能在单点测试通过！！！！ 还是要学习课本代码的写法！！！！！ 
int main(){
	char str[85][80];
	int i=0;
	while(scanf("%s",&str[i]) != EOF)
		i++;
	for(int j=i-1; j>=0; j--){
		printf("%s",str[j]);
		if(j) printf(" ");	
	}
	return 0;
}
#endif

#if(1)   //参考代码 
#include <cstdio>
#include <cstring>
int main(){
	char str[85];
	gets(str);
	int length = strlen(str);
	int r=0, h=0;  //r为行 h为列 
	char a[length][85];
	for(int i=0; i<length; i++){
		if(str[i] != ' ')
			a[r][h++] = str[i];
		else{
			a[r][h] = '\0';
			r++;
			h=0;
		}
	}
	for(int j=r; j>=0; j--){
		printf("%s",a[j]);
		if(j) printf(" ");
	}
	return 0;
}
#endif 
