"""
arg: vector<int> nums: 1个整数数组；
     int target：1个目标sum值；
return: vector<int>: 数组里存在2个数，它们的和等于target，返回它们的数组下标；
"""

class My_solution_1 {
# O(n²)+O(1)
# 简单的遍历数组
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res; 
        for (int i=0;i<nums.size()-1;i++) {
            for (int j=i+1;j<nums.size();j++) {
                if (nums[i] + nums[j] == target) {
                    res.push_back(i);
                    res.push_back(j);
                }
            }
        }
        return res;
    }
};

class Need_to_learn_1 {
# O(n)+O(n)
# 用hash判断过去是否存在某元素，使得此元素和当前元素的和等于target
# 注意: return不能只写在条件语句里，可以在条件语句外面返回空{}
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hash;
        for (int i=0; i<nums.size(); i++) {
            if (hash.find(target-nums[i]) != hash.end()) {
                return {hash[target-nums[i]], i};
            }
            hash[nums[i]] = i;
        }
        return {};
    }
};
