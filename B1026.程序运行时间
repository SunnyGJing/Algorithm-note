#include <cstdio>
int CLK_TCK = 100; 
int main(){
	int C1, C2, time, s;
	scanf("%d%d",&C1,&C2);
	if(C1>=C2) scanf("%d%d", &C1, &C2);
	time = C2 - C1;
	if(time%CLK_TCK>=50){
		s = time/CLK_TCK + 1;
	}
	else s = time/CLK_TCK;
	printf("%d:%d:%d",s/3600,s/60%60,s%60);
} 
