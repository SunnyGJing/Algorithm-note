#include <cstdio>    //已在code up通过    2018-01-13 12:57:24	 
#include <cstring>
bool Judge(int length, char str[]){
	for(int i=0; i<length/2; i++){
		if(str[i] != str[length-1-i])
			return false;
	}
		return true;
}
int main(){
	char str[260];
	gets(str);
	int length = strlen(str);
	bool flag = Judge(length, str);
	if(flag==true) printf("YES");
	else printf("NO");
} 
