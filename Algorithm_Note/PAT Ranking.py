#include <cstdio>  //已在pat通过   18年1月15日 17:53	
#include <cstring>
#include <algorithm>
using namespace std;
struct Student{
	char id[15];
	int score;
	int loc_num;
	int loc_r;
}stu[30000];
bool cmp(Student a, Student b){
	if(a.score!=b.score)  return a.score>b.score;
	else  return strcmp(a.id, b.id) < 0;
}
int main(){
	int n, k, num=0;
	scanf("%d",&n); //the number of test locations
	for(int i=1; i<=n; i++){
		scanf("%d",&k); //the number of testees
		for(int j=0; j<k; j++){
			scanf("%s %d",&stu[num].id,&stu[num].score);
			stu[num].loc_num = i;
			num++;
		}
		sort(stu+num-k, stu+num, cmp);
		stu[num-k].loc_r = 1;
		for(int q=num-k+1; q<num; q++){
			if(stu[q].score==stu[q-1].score) stu[q].loc_r=stu[q-1].loc_r;
			else stu[q].loc_r = q-(num-k)+1;
		}
	}
	printf("%d\n",num);
	sort(stu,stu+num,cmp);
	int r=1;
	for(int i=0; i<num; i++){
		if(i>0&&stu[i].score!=stu[i-1].score){
			r=i+1;
		}
		printf("%s %d %d %d\n",stu[i].id,r,stu[i].loc_num,stu[i].loc_r);
	}
	return 0;
} 
