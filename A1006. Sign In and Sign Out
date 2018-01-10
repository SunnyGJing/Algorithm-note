#if(0) //已在pat通过 18-01-10 19:12   （9ms	384kB) 
// 我的方法比课本的方法 时间复杂度小~~~~~~~~~~~~开心！！！！
// 但我从课本参考代码中学到了一个技巧！ 往下拖看看！！ 
#include <cstdio>
struct Person {
	char ID[20];
	int l_hh, l_mm, l_ss;    //leave time
	int c_hh, c_mm, c_ss;    //come  time
}temp, earlest, latest;
int main(){
	int n,early=1000000, late=-1, c_time, l_time;
	scanf("%d",&n);
	for(int i=0; i<n; i++){
		scanf("%s %d:%d:%d %d:%d:%d",&temp.ID,&temp.c_hh,&temp.c_mm,&temp.c_ss,&temp.l_hh,&temp.l_mm,&temp.l_ss);
		c_time=temp.c_hh*10000+temp.c_mm*100+temp.c_ss;
		l_time=temp.l_hh*10000+temp.l_mm*100+temp.l_ss;
		if(c_time<early){
			early = c_time;
			earlest = temp;
		}
		if(l_time>late){
			late = l_time;
			latest = temp;
		}
	}
	printf("%s %s\n",earlest.ID,latest.ID);
	return 0;
} 
#endif

#if(1) 
//这是我根据课本代码 做了一丢丢修改后的~~~~ 用了一个巧妙法子 代码简了好多~~~~ 学起来！！！！！~特别特别好！！！ 
// 把输入中的签到时间和离开时间分两个scanf，结构体中的时间无须分别定义签到时间和离开时间，就能一个变量两次用了~~~~~~ 
#include <cstdio>
struct Person {
	char ID[20];
	int hh, mm, ss;                     //这里简化了！！！！
}temp, earlest, latest;
int main(){
	int n,early=1000000, late=-1, c_time, l_time;
	scanf("%d",&n);
	for(int i=0; i<n; i++){
		scanf("%s %d:%d:%d",&temp.ID,&temp.hh,&temp.mm,&temp.ss);    //这里分两个scanf实现！！时间变量重复使用！！
		c_time=temp.hh*10000+temp.mm*100+temp.ss;
		if(c_time<early){
			early = c_time;
			earlest = temp;
		}
		scanf("%d:%d:%d",&temp.hh,&temp.mm,&temp.ss);
		l_time=temp.hh*10000+temp.mm*100+temp.ss;
		if(l_time>late){
			late = l_time;
			latest = temp;
		}
	}
	printf("%s %s\n",earlest.ID,latest.ID);
	return 0;
} 
#endif

#if(0)  // 参考代码       (12ms	384kB)
#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

struct pNode{
	char id[20];
	int hh,mm,ss; 
}temp, ans1, ans2; //ans1存放最早签到时间，ans2存放最晚签到时间 

bool great(pNode node1, pNode node2){ //node1的时间大于node2的时间则返回true
	if(node1.hh != node2.hh) return node1.hh > node2.hh;
	if(node1.mm != node2.mm) return node1.mm > node2.mm;
	return node1.ss > node2.ss;
}

int main(){
	int n;
	scanf("%d",&n);
	ans1.hh=24, ans1.mm=60, ans1.ss=60; //把初始签到时间设成最大
	ans2.hh=0, ans2.mm=0, ans2.ss=0; //把初始签离时间设成最小
	for(int i=0; i<n; i++){
		//先读入签到时间
		scanf("%s %d:%d:%d",&temp.id,&temp.hh,&temp.mm,&temp.ss);  
		if(great(temp, ans1) == false) ans1 = temp; //ans1取更小的签到时间
		//temp再作为签离时间读入 
		scanf("%d:%d:%d",&temp.hh,&temp.mm,&temp.ss);
		if(great(temp, ans2) == true) ans2 = temp; //ans3取更大的签离时间	 
	} 
	printf("%s %s\n", ans1.id, ans2.id);
	return 0; 
}
#endif 
