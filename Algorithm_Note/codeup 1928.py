#if(0)  //已在codeup通过  2018-01-12 09:34:30	耗时 71
// 时间复杂度比课本代码高了特别多！！！课本代码对时间变量的处理比我好，多看看！！！ 
#include <cstdio>
int a[13][2]={{0,0},{31,31},{28,29},{31,31},{30,30},{31,31},{30,30},{31,31},{31,31},{30,30},{31,31},{30,30},{31,31}};
int main(){
	int date1,date2,day1,month1,year1;
	while(scanf("%d%d",&date1,&date2)!=EOF){
		if(date2<date1){
			int temp=date1;
			date1=date2;
			date2=temp;
		}
		int ans = 1;
		while(  date1<date2 ){
			date1++;
			day1 = date1%100;
			month1 = date1%10000/100;
			year1 =date1/10000;
			if((year1%4==0&&year1%100!=0)||(year1%400==0)){
				if(day1==a[month1][1]+1){
					month1++;
					day1=1;
				}
			} 
			else if(day1==a[month1][0]+1){
				month1++;
				day1=1;
			}
			if(month1==13){
				year1++;
				month1=1;
			}
			ans++;
			date1=year1*10000+month1*100+day1;
		}
		printf("%d\n",ans);
	}
	return 0;
}
#endif

#if(0) //参考代码   耗时24 
#include <cstdio>
int month[13][2]={{0,0},{31,31},{28,29},{31,31},{30,30},{31,31},{30,30},{31,31},{31,31},{30,30},{31,31},{30,30},{31,31}};
bool isLeap(int year){
	return(year%4==0&&year%100!=0)||(year%400==0);
}
int main(){
	int time1,d1,m1,y1;
	int time2,d2,m2,y2;
	while(scanf("%d%d",&time1,&time2)!=EOF){
			time1=20180301;
		time2=20180401;
		if(time2<time1){
			int temp=time1;
			time1=time2;
			time2=temp;
		}
			d1 = time1%100, m1 = time1%10000/100, y1 =time1/10000;
			d2 = time2%100, m2 = time2%10000/100, y2 =time2/10000;
			int ans = 1;
			while(y1<y2||m1<m2||d1<d2){
				d1++;
				if(d1==month[m1][isLeap(y1)]+1){
					m1++;
					d1=1;
				}
				if(m1==13){
					y1++;
					m1=1;
			}
			ans++;
		}
		printf("%d\n",ans);
	}
	return 0;
}
#endif
