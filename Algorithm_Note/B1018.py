#if(0)     //虽然对，太复杂太笨拙！！！！
#include <cstdio>
const int maxn = 100010;
char a[maxn], b[maxn];
int main(){
	int n, jia, yi, ping, j1, b1, c1, j2, b2, c2;
	jia = yi = ping = j1=j2=b1=b2=c1=c2=0;
	scanf("%d",&n);
	
	for(int i=0; i<n; i++){
/*		a[i]=getchar();
		getchar();
		b[i]=getchar(); 
		getchar(); */
		getchar();
		scanf("%c %c",&a[i],&b[i]);
	}
	for(int j=0; j<n; j++){
		if(a[j]=='B'){
		 	if(b[j]=='C'){
		 		jia++; b1++;
			 }
			else if(b[j]=='J'){
				yi++, j2++;
			}
			else ping++; 
		} 
		if(a[j]=='C'){
		 	if(b[j]=='J'){
		 		jia++; c1++;
			 }
			else if(b[j]=='B'){
				yi++, b2++;
			}
			else ping++;
		} 
		if(a[j]=='J'){
		 	if(b[j]=='B'){
		 		jia++; j1++;
			 }
			else if(b[j]=='C'){
				yi++, c2++;
			}
			else ping++;
		} 
	}
	int max1,max2;
	char ans1, ans2;
	max1=b1;
	if(max1<c1){
		max1 = c1;
		ans1 = 'C';
	}
	else if(max1<j1){
		max1 = j1;
		ans1 = 'J';
	}
	else ans1 = 'B';
	max2=b2;
	if(max2<c2){
		max2 = c2;
		ans2 = 'C';
	}
	else if(max2<j2){
		max2 = j2;
		ans2 = 'J';
	}
	else ans2 = 'B';
	printf("%d %d %d\n",jia,ping,yi);
	printf("%d %d %d\n",yi,ping,jia);
	printf("%c %c",ans1,ans2);
}
#endif

#if(1)
#include <cstdio>
int change(char c){  
	if(c == 'B') return 0;
	if(c == 'C') return 1;
	if(c == 'J') return 2; //恰好是循环相克顺序，且字典序递增 
}
int main(){
	char mp[3] = {'B','C','J'};
	int n;
	scanf("%d",&n);
	int times_A[3] = {0}, times_B[3] = {0}; //分别记录甲、乙的胜、平、负次数 
	int hand_A[3] = {0}, hand_B[3] = {0}; //按BCJ顺序分别记录甲乙3种手势获胜次数 
	char c1, c2;
	int k1, k2;
	for(int i = 0; i < n; i++){
		getchar();
		scanf("%c %c",&c1,&c2); //甲乙的手势 
		k1 = change(c1);        //转换为数字 
		k2 = change(c2);
		if((k1 + 1) % 3 == k2){ //如果甲赢 
			times_A[0]++;
			times_B[2]++;
			hand_A[k1]++;
		} else if(k1 == k2){
			times_A[1]++;
			times_B[1]++;
		} else {
			times_A[2]++;
			times_B[0]++;
			hand_B[k2]++;
		} 
	}
	printf("%d %d %d\n", times_A[0], times_A[1], times_A[2]);
	printf("%d %d %d\n", times_B[0], times_B[1], times_B[2]);
	int id1 = 0, id2 = 0;
	for(int i=0; i < 3; i++){
		if(hand_A[i] > hand_A[id1]) id1 = i;
		if(hand_B[i] > hand_B[id1]) id2 = i;
	}
	printf("%c %c\n", mp[id1], mp[id2]); //转变回BCJ
	return 0; 
}
#endif
