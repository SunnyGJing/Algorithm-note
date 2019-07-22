#include <iostream>
#include <unordered_map>
using namespace std;

int main() {

    unordered_map<int,int> hash;
    hash[1]=1;
    hash[2]=3;
    
    // 计算某个key的个数
    cout << hash.count(2) << endl;
    
    // 清除hash中的所有<key,value>对
    hash.clear();
    cout << hash.size() << endl; // 输出“0”
    
    // 如下所示：访问hash中不存在的key，并不会报错，因为key已经被自动添加到hash中，value为0
    cout << "hash[3]: " << hash[3] << endl;
    cout << hash.size() << endl; // 输出“1”
    
    // 遍历hash，打印所有键值对
    for(auto& v:hash) {
        cout<<v.first<<" "<<v.second<<endl;
    }
    // 同上
    for(unordered_map<int, int>::iterator iter=hash.begin(); iter!=hash.end(); iter++) {
        cout << iter->first << " " << iter->second << endl;
    }
}
