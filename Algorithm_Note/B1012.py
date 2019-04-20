#if(0)
#include <cstdio>
int main(){
	int a[1010] = {0}; 
	int A1=0, A2=0, A5=0;
	int count1=0, count2=0,count3=0,count4=0,count5=0;
	int n, r, sum = 0;
	double A4; 
	scanf("%d",&n);
	for(int i = 0; i < n; i++){
		scanf("%d",&a[i]);
	}
	for(int i = 0; i< n; i++){
		if(a[i]%5 == 0 && a[i]%2 == 0){
			A1 += a[i];	
			count1++;
		}
		if(a[i]%5 == 1){
			if(count2%2 == 0) A2 += a[i];
			else A2 -= a[i];
			count2++;
		}
		if(a[i]%5 == 2) count3++;
		if(a[i]%5 == 3){
			sum+=a[i];
			count4++;
		}
		if(a[i]%5 == 4 && A5<a[i]){
			A5 = a[i];	
			count5++;
		}
	}
	if(count4!=0){
		r = sum*10/count4;
		if(r%10>=5) r += 1;
		A4 = (double)r/10;
	}
	if(count1 != 0) printf("%d ",A1);
		else printf("N ");
	if(count2 != 0) printf("%d ",A2); 
		else printf("N ");
	if(count3 != 0) printf("%d ",count3);
		else printf("N "); 
	if(count4 != 0) printf("%lf ",A4);
		else printf("N "); 
	if(count5 != 0) printf("%d",A5);
		else printf("N"); 
	return 0;
}
#endif

#if(1)
#include <cstdio>
int main(){
	int count[5] = {0};
	int ans[5] = {0}; 
	int n, temp;
	scanf("%d",&n);
	for(int i = 0; i < n; i++){
		scanf("%d",&temp);
		if(temp%5 == 0 && temp %2 == 0){
			ans[0] += temp;	
			count[0]++;
		}
		if(temp%5 == 1){
			if(count[1]%2 == 0) ans[1] += temp;
			else ans[1] -= temp;
			count[1]++;
		}
		if(temp%5 == 2) count[2]++;
		if(temp%5 == 3){
			ans[3] += temp;
			count[3]++;
		}
		if(temp%5 == 4){
			if(ans[4] < temp){
				ans[4] = temp;
			}				
			count[4]++;
		}
	}
	if(count[0] != 0) printf("%d ",ans[0]);
		else printf("N ");
	if(count[1] != 0) printf("%d ",ans[1]); 
		else printf("N ");
	if(count[2] != 0) printf("%d ",count[2]);
		else printf("N "); 
	if(count[3] != 0) printf("%.1f ",(double)ans[3]/count[3]);   //保留 1 位小数 
		else printf("N "); 
	if(count[4] != 0) printf("%d",ans[4]);
		else printf("N"); 
	return 0;
}
#endif 
