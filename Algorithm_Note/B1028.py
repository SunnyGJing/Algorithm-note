#if(1) //2018-01-10 14:51 已在pat通过
// 和课本上给的代码不一样，自认为我的方法更好更适合我，抽空看看课本的思路吧！！！ 
#include <cstdio>
const int today = 20140906;
const int ago = 18140906;
struct Person {
	char name[10];
	int year;
	int month;
	int day;
}temp,oldest,youngest;
int main(){
	int n, time, count=0,remote=today, resent=ago;
	scanf("%d",&n);
	for(int i=0; i<n; i++){
		scanf("%s %d/%d/%d",temp.name,&temp.year,&temp.month,&temp.day);
		getchar();
		time = temp.year*10000+temp.month*100+temp.day;
		if(time<=today&&time>=ago){
			count ++;
			if(time>=resent){
				resent = time;
				youngest = temp;
			}
			if(time<=remote){
				remote = time;
				oldest = temp;
			}
		}
	}
	if(count)
		printf("%d %s %s\n",count,oldest.name,youngest.name);
	else
		printf("0\n");
} 
#endif
 
#if(0) // 18-01-09 
//提交到pat部分正确！！有一个结果不正确，原因待查？？？？？ 
#include <cstdio>
struct Person {
	char name[10];
	int year, month, day;
}temp, maxn, minn;    //存数据， 年龄最大， 年龄最小 
const int today = 20140906; 
const int ago = 18140906;
int main(){
	int n, time, count=0, remotest = today+1, nearest = ago-1;
	scanf("%d",&n);
	for(int i=0; i<n; i++){
		scanf("%s %d/%d/%d",&temp.name,&temp.year,&temp.month,&temp.day);
		getchar(); // 吃掉空格  
		time = temp.year*10000+temp.month*100+temp.day;// 出生时间表示成数字，便于比较 
		if(time<=today&&time>=ago){ //出生时间不符合条件的，忽略不操作 
			count++;
			if(nearest<time){
				nearest = time;
				minn= temp; // 找年龄最小的 
			} else if(remotest>time){
				remotest = time;
				maxn = temp; // 找年龄最大的 
			}
		}
	}
	if(count!=0){
	printf("%d %s %s",count,maxn.name,minn.name);	
	} else printf("0"); // 考虑特殊情况（满足条件的出生时间数为0） 
	return 0;
} 
