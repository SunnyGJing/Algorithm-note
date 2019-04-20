#if(0)    //已在pat通过 18-1-13 07:50	学一下参考代码对回文判断的处理（比我的好） 
#include <cstdio>    
int main(){
	int n, b;
	scanf("%d%d",&n,&b);
	//十进制转b进制 
	int i = 0, a[40] = {0};
	do{
		a[i++] = n % b;
		n /= b;
	}while(n);  
	//判断回文字 
	int k = i/2; //（记）循环结束时 i 为 length； i-1 为最高位数组下标 
	int count = 0;
	for(int j=0; j<k; j++){
		if(a[j] == a[i-j-1]) count++;
	}
	if(count==k) printf("Yes\n");
	else printf("No\n");
	for(i--; i>=0; i--){
		printf("%d",a[i]); 
		if(i) printf(" ");
	}
		
	return 0;
} 
#endif

#if(1)  //参考代码
#include <cstdio>   //参考代码
bool Judge(int b[], int length){
	for(int i=0; i<length/2; i++){
		if(b[i]!=b[length-1-i])
			return false;
	}
	return true; //所有位置都对称 
} 
int main(){
	int n, b;
	scanf("%d%d",&n,&b);
	int num = 0, a[40] = {0};
	do{
		a[num++] = n % b;
		n /= b;
	}while(n);  
	bool flag = Judge(a, num); 
	if(flag==true) printf("Yes\n");
	else printf("No\n");
	for(int i=num-1; i>=0; i--){
		printf("%d",a[i]); 
		if(i) printf(" ");
	}
		
	return 0;
} 
#endif 
