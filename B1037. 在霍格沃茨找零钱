#if(0)     //已在pat通过   18-01-12 22:10       学习一下参考代码！特别简练！ 
#include <cstdio>   
int sign = 0;
int main(){
	int P, A;
	int a[3];
	scanf("%d.%d.%d",&a[0],&a[1],&a[2]);
	P = a[2]+a[1]*29+a[0]*17*29;
	scanf("%d.%d.%d",&a[0],&a[1],&a[2]);
	A = a[2]+a[1]*29+a[0]*17*29;  //算出应付 P和实付 A
	int x;
	if(P<=A) x = A - P;
	else{
		sign = 1;
		x = P - A;
	}
	a[2] = x%29;
	a[1] = x/29%17;
	a[0] = x/29/17;
	if(sign)
		printf("-%d.%d.%d",a[0],a[1],a[2]);
	else
		printf("%d.%d.%d",a[0],a[1],a[2]);

}
#endif

#if(1)        //参考代码   简练！！！学习！！！！ 
#include <cstdio>   
const int Galleon = 17*29;   //1个Galleon兑换17*29个Knut
const int Sickle = 29;       //1个Sickle兑换29个Knut 
int main(){
	int a1,b1,c1;
	int a2,b2,c2; 
	scanf("%d.%d.%d %d.%d.%d",&a1,&b1,&c1,&a2,&b2,&c2);
	int price = c1 + b1 * Sickle + a1 * Galleon;  //价格，兑换成Knut单位 
	int money = c2 + b2 * Sickle + a2 * Galleon;  //付款，兑换成Knut单位 
	int change = money - price;    
	if(change<0){
		printf("-");
		change = -change;
	}
	printf("%d.%d.%d\n",change/Galleon, change%Galleon/Sickle,change%Sickle);
	return 0;
}
#endif 
