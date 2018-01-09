/********************************/
/* 害死人不偿命的 （3n+1) 猜想  */
/********************************/ 
#include <stdio.h>
int main()
{
	int n, t, step = 0;
	scanf("%d",&n);
	while( n <= 0 || n > 1000 )
		scanf("%d",&n);	
	while( n!=1 ){
		if( n % 2 == 0 )                //如果是偶数 
			n = n / 2;
		else                          //如果是奇数 
			n = (3 * n + 1) / 2;
		step ++;                    //计数器加 1 
	}
	printf("%d\n",step);
	return 0;
 } 
