#include <cstdio>   //  已在pat通过  18年1月13日 15:11	 
#include <cstring>
int main(){
	char str[1010];
	gets(str);
	int len = strlen(str);
	int ans[10]={0};
	for(int i=0; i<len; i++){
		ans[str[i]-'0']++; 
	}
	for(int k=0; k<10; k++){
		if(ans[k]){
			printf("%d:%d\n",k,ans[k]);
		}
	}
	return 0;
} 
