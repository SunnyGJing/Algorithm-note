#include <cstdio>  // 已在pat通过  18年1月13日 15:58  虽然通过了pat 但是发现了一处错误 第25行必须加上那一句判定！！！！！
// 看课本代码思维严谨，多看看！！（我没敲上来） （ps 要改用bool型flag哦） 
const int a[17]={7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2};
const char b[12]={'1','0','X','9','8','7','6','5','4','3','2'};
int main(){
	int n;
	bool flag = true; 
	scanf("%d",&n);
	getchar(); 
	while(n--){
		char str[20];
		gets(str);
		int ans=0;
		for(int i=0; i<17; i++){
			if(str[i]-'0'<0&&str[i]-'0'>9){
				printf("%s\n",str);
				flag = false;
				break;	
			}
			else
				ans += (str[i]-'0') * a[i];		
		}
		int z = ans%11;
		char m = b[z];
		if(flag == true && m!=str[17]){        //这里必须加 flag==true！！！！！！！！ 
			flag = false;
			printf("%s\n",str);
		}
	}
	if(flag == true) printf("All passed\n");
	return 0;
}
