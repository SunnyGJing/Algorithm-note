#if(0)  //已在pat通过  18年1月13日 09:18	 还是没有课本代码巧，学习！！！！！ 
#include <cstdio>
int num, ans[2];
void init(){
	num = 0;
	ans[0]=0, ans[1]=0;
}
int main(){
	int x;
	printf("#");
	for(int j=0; j<3; j++){
		scanf("%d",&x);
		init();
		do{
			ans[num++] = x%13;
			x /= 13;
		}while(x);
		for(int k=1; k>=0; k--){
			if(ans[k]<10)
				printf("%d",ans[k]);
			else
				printf("%c",'A'+(ans[k]-10));   //关键！！！！！！成功实现了 很开心~ 
		}
	}
	return 0;
}
#endif

#if(1)    //参考代码 
#include <cstdio>
char radix[13]={
	'0','1','2','3','4','5','6','7','8','9','A','B','C'
};
int main(){
	int r, g, b;
	scanf("%d%d%d",&r, &g, &b);
	printf("#");
	printf("%c%c", radix[r/13], radix[r%13]);
	printf("%c%c", radix[g/13], radix[g%13]);
	printf("%c%c", radix[b/13], radix[g%13]);
	return 0;
}
#endif 
