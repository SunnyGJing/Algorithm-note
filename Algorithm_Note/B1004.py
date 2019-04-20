#if(1) // 18-01-10 10:48 已在pat通过 
#include <cstdio>
const int maxn = 15;
struct Student {
	char name[maxn];
	char id[maxn];
	int score;
}temp, ans_max, ans_min;//temp存放临时数据、ans_max为最高分数的学生、ans_min为最低分数的学生
 
int main(){
	int n;
	scanf("%d",&n);
	ans_max.score = -1; 
	ans_min.score = 101; //初始化最高、最低分数 
	for(int i=0; i<n; i++){
		scanf("%s%s%d",temp.name,temp.id,&temp.score);
		getchar();
		if(temp.score > ans_max.score) ans_max = temp;  //该学生分数更高，更新 
		if(temp.score < ans_min.score) ans_min = temp;  //该学生分数更低，更新
	}
	printf("%s %s\n",ans_max.name,ans_max.id);
	printf("%s %s\n",ans_min.name,ans_min.id);
	return 0;
} 
#endif
 
#if(0)
//不对哦！！！看书！ 学到了结构体的输入与输出以及赋值
#include <cstdio>
struct student {
	char name[10];
	char Id[10];
	int score ;
}students[100];
int main(){
	int n,s,max=0, min=0, maxI, minI;
	char c;
	scanf("%d",&n);
	for(int i=0; i<n; i++){ 
		int j = 0,k = 0; 
		while((c=getchar())!=' '){
		students[i].name[j++] = c; 
		}
		while(c=getchar()!=' '){
		students[i].Id[k++] = c; 
		}
		scanf("%d",&s);
		students[i].score = s;
		if(max<s){
			max=students[i].score;
			maxI = i;
		}
		else if(min>s){
			min=students[i].score;
			minI = i;
		} 
	}
	printf("%s",students[maxI].name);
	printf(" ");
	printf("%s",students[maxI].Id);
	printf("\n");
	printf("%s",students[minI].name);
	printf(" ");
	printf("%s",students[minI].Id);
	return 0;
} 
#endif
