#if(0)      // 已在pat通过  18年1月14日 14:43    往下翻翻！！学到了把int型数字按位写到char型数组的简单办法！！！ 
#include <cstdio>   
#include <cstring>
const char a[10][7]={"zero","one","two","three","four","five","six","seven","eight","nine"};
int main(){
	char str[110];
	gets(str);
	int len = strlen(str);
	int sum = 0;
	for(int i=0; i<len; i++){
		sum += str[i] - '0';
	}
	int num=0, ans[5];
	do{
		ans[num++] = sum%10;
		sum /= 10;
	}while(sum);
	for(int j= num-1; j>=0; j--){
		printf("%s",a[ans[j]]);
		if(j) printf(" ");
	}
	return 0;
}
#endif

#if(1)        // 把int型数字按位写到char型数组的简单办法（sprintf函数）
#include <cstdio>    
#include <cstring>
const char a[10][7]={"zero","one","two","three","four","five","six","seven","eight","nine"};
int main(){
	char str[110];
	gets(str);
	int len = strlen(str);
	int sum = 0;
	for(int i=0; i<len; i++){
		sum += str[i] - '0';
	}
	
	char digit[10];
	sprintf(digit,"%d",sum);      //一句代码代替了do while~~~~~简单！！！ 学习！！！！ 
	
	for(int i=0; digit[i]!='\0';i++){   //注意，同时输出也变了！
		printf("%s",a[digit[i]-'0']);
		if(digit[i+1]!='\0') printf(" ");
	}
	return 0;
}
#endif
