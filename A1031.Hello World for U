#include <cstdio>
int main(){
	char ch[100], c;
	int i=0, r, n, length; 
	while((c=getchar())!=EOF){
		 ch[i] = c;
		 i++;
	} //输入字符数组，while循环结束时 i-1=字符串总长度
	 length = i -1;
	 r = (length+2)/3; //行数
	 n = (length+2)/3 +(length+2)%3; //底层个数
	 // 输出各行（除去尾行） 
	 for(int j=0; j<r-1; j++){
	 	printf("%c",ch[j]); //输出单行首字符 
	 	for(int k=0; k<n-2; k++)
	 		printf(" "); //输出空格 
	 	printf("%c\n",ch[length-1-j]); 
	 } 
	 // 输出尾行
	 for(int j=r-1; j<r+n-1; j++){
	 	printf("%c",ch[j]);
	 } 
}

/* 正确~~ 但如下技巧需要掌握
	上面第5行代码 	while((c=getchar())!=EOF){
					 ch[i] = c;
					 i++;	} 
	我这样写，本想用gets(ch); 但考虑到需要记字符串长度，改用循环计数 
	看课本发现，可以用库函数简化！！！！一句代码就能获取长度！！！ （如下） 
	#include <cstring>
	int N = strlen(ch);  */  
