#if(1)//18.01.10 8:23  已在pat通过
#include <cstdio>
const int maxn = 1010; 
struct Student {
	long long id;  //准考证号 
	int examSeat;  //考试座位号 
} testSeat[maxn];  //试机座位号作为下标来记录学生 
int main(){
	int n,m,seat,examSeat;
	long long id;
	scanf("%d", &n);    //考生人数 
	for(int i=0; i<n; i++){
		scanf("%lld %d %d",&id,&seat,&examSeat); //准考证号、试机座位号、考试座位号 
		testSeat[seat].id = id;
		testSeat[seat].examSeat = examSeat;
	}
	scanf("%d",&m);    //查询个数 
	for(int i=0; i<m; i++){
		scanf("%d",&seat);
		printf("%lld %d\n",testSeat[seat].id,testSeat[temp].examseat);	
	}
	return 0;
}
#endif

#if(0)//18.01.09
//基本实现！有一句不对！！！！！！   看课本学习结构体！！ 
#include <cstdio>
const int maxn=1010;
int a[maxn][3]={0};
int main(){
	int n, m, temp;
	long long num, numb ;
	scanf("%d",&n);
	for(int i=0; i<n; i++){
		scanf("%lld%d%d",&num,&a[i][1],&a[i][2]);
		a[i][0] = num % 1000;
		numb = num/1000;            //这地方不对！！！！！！！为啥呢？？？、 
		for(int j=0; j<i; j++){
			if(a[i][0]==a[j][0]||a[i][1]==a[j][1]||a[i][2]==a[j][2]){
				scanf("%lld%d%d",&num,&a[i][1],&a[i][2]);
				a[i][0] = num % 1000;
			} //输入保证每个人的准考证号不同、试机座位号不同、考试座位号不同 
//		 printf("num=%lld %d %d %d",num,a[0][0],a[0][1],a[0][2]); 
		}
	}
	scanf("%d",&m);
	for(int i=0; i<m; i++){
		scanf("%d",&temp);
		for(int j=0; j<n; j++){
			if(temp==a[j][1])
				printf("%d%03d %d\n",numb,a[j][0],a[j][2]);     2353663919
		}
	}
	return 0;
}
#endif
