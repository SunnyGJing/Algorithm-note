#if(0)       // 出错！！ 
#include <cstdio>
#include <cmath>
int main(){
	char A[10], B[10];
	int Da, Db, n1, n2, Pa, Pb, result;
	n1 = n2 = Pa = Pb = 0;
	gets(A);
	scanf("%d",&Da);
	getchar();
	gets(B);
	scanf("%d",&Db);
	for(int i=0; A!='\0'; i++){
		if(A[i] == Da){
			Pa += Da * pow(10, n1);
			n1 ++;
		}
	} 
	for(int i=0; B!='\0'; i++){
		if(B[i] == Db){
			Pb += Db * pow(10, n2);
			n2 ++;
		}
	} 
	result = Pa + Pb;
	printf("%d",result);
}
#endif

#if(1)
#include <cstdio>
int main(){
	long long a, b, da, db;
	scanf("%lld%lld%lld%lld",&a, &da, &b, &db);
	long long pa = 0, pb = 0;
	while(a !=0){
		if(a%10==da) pa = pa * 10 + da;
		a = a / 10;
	}
	while(b !=0){
		if(b%10==db) pb = pb * 10 + db;
		b = b / 10;
	}
	printf("%lld", pa + pb);
	return 0;
}
#endif
