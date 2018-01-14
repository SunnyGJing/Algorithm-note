#include <cstdio>   // 已在pat通过  18年1月14日 16:16	可以看一下课本代码（用结构体实现） 没有敲上来~ P79 
#include <cstring>
int main(){
	char team[1000][15], sec[1000][15];
	int n, numb[1000], count=0, k=0;
	bool Judge = true;
	scanf("%d",&n);
	for(int i=0; i<n; i++){
	scanf("%s %s",&team[i],&sec[i]);
	} 
	for(int i=0; i<n; i++){
		int len=strlen(sec[i]);
		for(int j=0; j<len; j++){
			if(sec[i][j]=='1'||sec[i][j]=='l'||sec[i][j]=='0'||sec[i][j]=='O'){
				Judge = false;
				if(sec[i][j]=='1') sec[i][j]='@';
				if(sec[i][j]=='l') sec[i][j]='L';
				if(sec[i][j]=='0') sec[i][j]='%';
				if(sec[i][j]=='O') sec[i][j]='o';
			}
		}
		if(Judge==false){
			count++;
			numb[k++] = i;
			Judge = true;	
		}
	}
	if(count == 0){
		if(n>1) printf("There are %d accounts and no account is modified\n",n);
		else printf("There is 1 account and no account is modified\n");
	} 
	else{
		printf("%d\n",count);
		for(int m=0; m<count; m++)
			printf("%s %s\n",team[numb[m]],sec[numb[m]]);
	}
	return 0;
} 
