#if(0) // 已在pat通过 18-01-10 16:30   (10ms	384kB)
//关于“四舍五入”疑问的解答：就算示例结果四舍五入了，题目只要没要求就无需四舍五入。（虽然看示例结果觉得程序写错了，没关系的）
//比参考代码的复杂度高，差在“寻找某一行的最大值”的处理上，学习这道题的参考代码是怎么处理的！！！！ 
#include <cstdio>
int main(){
	char ans[3];
	double w,t,l, max, result=1;
	for(int i=0; i<3; i++){
		scanf("%lf %lf %lf",&w,&t,&l);
		max = w;
		ans[i] = 'W';
		if(t>max){
			max = t;
			ans[i] = 'T';	
		} 
		if(l>max){
			max = l;
			ans[i] = 'L';
		}
		result *= max;
	}
	result = (result * 0.65 -1) * 2;
	printf("%c %c %c %.2f",ans[0],ans[1],ans[2],result);
	return 0;
} 
#endif

#if(1)  // 参考代码   (6ms	384kB) 
#include <cstdio>
char S[3] = {'W', 'T', 'L'};
int main(){
	double ans = 1.0, tmp, a;
	int idx; //记录每行最大数字的下标
	for(int i=0; i<3; i++){
		tmp = 0.0;
		for(int j=0; j<3; j++){ //寻找该行最大的数字存于tmp 
			scanf("%lf",&a);
			if(a > tmp){
				tmp = a;
				idx = j;
			}
		}
		ans *= tmp;
		printf("%c ",S[idx]);
	} 
	printf("%.2f",(ans*0.65 -1) *2);
	return 0;
}
#endif

#if(0) // (9ms	512kB) 
// 若输入为多次（行），输出结果作为一个整体分属于各次输入，以“一次输入一次输出，输入与输出交杂”为思路，竟然也是正确的！！
// 常规思路是“全部遍历（或保存）后，再输出”。 
#include <cstdio>
int main(){
	double w, t, l, max, result=1;
	char ans;
	for(int i=0; i<3; i++){
		scanf("%lf %lf %lf",&w,&t,&l);
		max = w;
		ans = 'W';
		if(t>max){
			max = t;
			ans = 'T';
		}
		if(l>max){
			max = l;
			ans = 'L';
		}
		result *= max;
		printf("%c ",ans);	
	}
	result = (result*0.65-1)*2;
	printf("%.2f\n",result);
}
#endif
