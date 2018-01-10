#if(0) // 已在pat通过 18-01-10 15:16 
// 本以为自己的代码比课本代码更简就算是更优 但在对比pat的时间复杂度后发现
// 我的思路：“每赋值一次便更新一次max，省去了单独枚举的过程”时间复杂度上升了。。。 
// 课本的思路：“先依次赋值，全部完成后，再枚举更新max”更好一些！！！  学习了！！！ 
#include <cstdio>
const int maxn = 100010;
int school[maxn]={0}; //学校编号为下标 存放该学校的总分 
int main(){
	int n, schID, score, ans_max=-1, ans_schID;
	scanf("%d",&n);
	for(int i=0; i<n; i++){
		scanf("%d%d",&schID,&score); 
		school[schID] += score;
		if(ans_max<school[schID]){
			ans_max = school[schID];
			ans_schID = schID;
		}
	}
	printf("%d %d\n",ans_schID,ans_max);
	return 0;
} 
#endif

 #if(1)    // 参考代码 
 #include <cstdio>
 const int maxn = 100010;
 int school[maxn] = {0};        //记录每个学校的总分
 int main(){
 	int n, schID, score;
 	scanf("%d",&n);
	for(int i = 0; i < n; i++){  //记录各学校总分 
	scanf("%d%d", &schID, &score);
 	school[schID] += score;
	} 
 int k = 1, MAX = -1;
 for(int i = 1; i <= n; i++){  //从所有学校中选出总分最高的一个 
 	if(school[i] > MAX){
 		MAX = school[i];
 		k = i;
	 }
 }
 printf("%d %d", k, MAX);
 return 0;
 }
 #endif

#if(0)        //错的   18-01-07
#include <cstdio>
int main(){
	int N, i, j, sch = 1, max, num;
	int score[100000][2];
	while(scanf("%d",&N) != EOF){
		for(i = 0; i < N; i++){
			scanf("%d%d",&score[i][0], &score[i][1]);
		}
	}
	for(i = 0; i < N; i ++){
		if(sch < score[i][0])  sch = score[i][0];
	}
	int total[sch][2]={0};
	for(i = 0; i < N; i ++){
		j = score[i][0];
		total[j-1][0] = j;
		total[j-1][1] += score[i][1];
	}
	num = total[0][0];
	max = total[0][1];
	for(i = 0; i < sch; i ++){
		if(max < total[i][1]){
			num = total[i][0];
			max = total[i][1];
		}
	}
	printf("%d %d",num,max);
	return 0;
 } 
 #endif
