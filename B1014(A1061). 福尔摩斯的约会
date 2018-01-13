#include <cstdio> //已在pat通过  2018年1月13日 20:23	有几个地方需要注意（用注释标注好了） 
const char Day[7][4]={"MON","TUE","WED","THU","FRI","SAT","SUN"};
int main(){
	char str[4][65];
	for(int i=0; i<4; i++){
		gets(str[i]);
	}

	int j;
	for(j=0; (str[0][j]!='\0')&&(str[1][j]!='\0'); j++){
		if((str[0][j]==str[1][j])&&(str[0][j]>='A')&&(str[0][j]<='G')){ //注意到'G'而不是'Z' 
			printf("%s ",Day[str[0][j]-'A']);
			break;
		}		
	}
	for( j++; (str[0][j]!='\0')&&(str[1][j]!='\0'); j++){  // 到这里先要j++ 
		if(str[0][j]==str[1][j]){
			if((str[0][j]>='A')&&(str[0][j]<='N')){
				printf("%02d:",(str[0][j]-'A')+10);  //必须补全两位 
				break;             //必须有break 
			}
			if((str[0][j]>='0')&&(str[0][j]<='9')){
				printf("%02d:",str[0][j]-'0');  //必须补全两位 
				break;             //必须有break 
			}
		}
	}
	for(int k=0; (str[2][k]!='\0')&&(str[3][k]!='\0');k++){
		if(str[2][k]==str[3][k]){
			if((str[2][k]>='A'&&str[2][k]<='Z')||(str[2][k]>='a'&&str[2][k]<='z')){ //一开始误以为大小写的ASC码连续 
				printf("%02d\n",k);   //必须补全两位 
				break;         //必须有break 
			}
		}	
	}
	return 0;
} 
