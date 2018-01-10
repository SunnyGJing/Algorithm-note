#if(0) //已在pat通过  18-01-10 20:31
// 但是！！有一个思路不如课本的代码！！关于变量max、min和结构体max、min，希望自己能学习并内化！！！
// 往下拖！！ 下面有我根据课本改的代码！ 
#include <cstdio>
const int maxn = 110;
struct Student {
	char name[15], id[15];
	int score;
}temp, max_female, min_man;   //学生成绩为数组下标

int main(){
	int n, f_max = -1, m_min = 101;
	char gender;
	scanf("%d",&n);
	for(int i=0; i<n; i++){
		scanf("%s %c %s %d",&temp.name,&gender,&temp.id,&temp.score);
		getchar();
		if(gender=='F'){
			if(temp.score>f_max){   //女生且分数高于当前f_max的分数 
				f_max = temp.score;
				max_female = temp;
			}
		}
		else if(temp.score<m_min){  //男生且分数低于当前m_min的分数  
				m_min = temp.score;
				min_man = temp;
			}
	}
	if(f_max == -1) printf("Absent\n");    //没有女生 
	else printf("%s %s\n",max_female.name,max_female.id);
	if(m_min == 101) printf("Absent\n");   //没有男生 
	else printf("%s %s\n",min_man.name,min_man.id);
	if(f_max == -1 || m_min == 101) printf("NA");  //没有男生或女生 
	else printf("%d\n",max_female.score - min_man.score);
	return 0;
} 
#endif

#if(1) // 这是我把我的代码 根据课本的代码做了一丢丢修改，有一个特别特别好的思想！！应该学习和内化！！！！！！
// 已经定义了临时、最大者和最小者这三个结构体，无须再单独定义变量max和min，直接用结构体！！然后覆盖(有一个好处：覆盖操作完成了更新最值的操作） 
#include <cstdio>
const int maxn = 110;
struct Student {
	char name[15]; 
	char id[15];
	int score;
}temp, max_female, min_man;   //学生成绩为数组下标
void init(){ //初始化女生最高成绩和男生最低成绩 
	max_female.score = -1;
	min_man.score = 101;
}
int main(){
	init();
	int n;
	char gender;
	scanf("%d",&n);
	for(int i=0; i<n; i++){
		scanf("%s %c %s %d",temp.name,&gender,temp.id,&temp.score);
		getchar();
		if(gender=='F' && temp.score>max_female.score)   //女生且分数高于当前f_max的分数 
				max_female = temp;
		else if(gender=='M' && temp.score<min_man.score)  //男生且分数低于当前m_min的分数  
				min_man = temp;
	}
	if(max_female.score == -1) printf("Absent\n"); //没有女生 
	else printf("%s %s\n",max_female.name,max_female.id);
	if(min_man.score == 101) printf("Absent\n");  //没有男生 
	else printf("%s %s\n",min_man.name,min_man.id);
	if(max_female.score == -1 || min_man.score == 101) printf("NA"); //没有男生或女生 
	else printf("%d\n",max_female.score - min_man.score);
	return 0;
} 
#endif 
