#if(1)  // 已在pat通过  18年1月13日 10:43  有两种方法：一种是统一单位再求和（me），另一种是依次进位法（课本）。
//	 统一单位再求和需要注意是否会溢出！！这道题需要用long long型存储数据！！！！！ 
#include <cstdio>
const long long Galleon = 17*29;
const long long Sickle = 29;
int main(){
	long long g1, g2, s1,s2, k1,k2;
	scanf("%lld.%lld.%lld %lld.%lld.%lld",&g1,&s1,&k1,&g2,&s2,&k2);
	long long a = g1*Galleon + s1*Sickle + k1;
	long long b = g2*Galleon + s2*Sickle + k2;
	long long x = a + b;
	printf("%lld.%lld.%lld",x/Galleon,x/Sickle%17,x%Sickle);
	return 0;
} 
#endif

#if(0)     //参考代码  方法：依次进位法 
#include <cstdio>
int main(){
	int a[3],b[3],c[3];
	scanf("%d.%d.%d %d.%d.%d",&a[0],&a[1],&a[2],&b[0],&b[1],&b[2]); //从高位到低位存储
//	int carry = 0;
	c[2] = (a[2] + b[2]) % 29;
	int carry = (a[2] + b[2]) / 29;  //进位 
	c[1] = (a[1] + b[1] + carry) % 17;
	carry = (a[1] + b[1] +carry ) / 17;
	c[0] = a[0] + b[0] + carry;
	printf("%d.%d.%d",c[0],c[1],c[2]);
	return 0;
}
#endif 
