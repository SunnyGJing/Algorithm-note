#include <vector>
using namespace std;

int main() {
    //1. Initializing like arrays :
    vector<int> vect{ 10, 20, 30 };

    //2. Specifying size and initializing all values :
    // Create a vector of size n with
    // all values as 10.
    int n = 3;
    vector<int> vect(n, 10);

    //3. Initializing by one by one pushing values :
    // Create an empty vector
    vector<int> vect; 
    vect.push_back(10);
    vect.push_back(20);
    vect.push_back(30);

    //4. Initializing from array :
    int arr[] = { 10, 20, 30 };
    int n = sizeof(arr) / sizeof(arr[0]);
    vector<int> vect(arr, arr + n);

    //5. Initializing from another vector :
    vector<int> vect1{ 10, 20, 30 };
    vector<int> vect2(vect1.begin(), vect.end());

    return 0;
}