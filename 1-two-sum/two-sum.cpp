class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> hmap;
        vector<int> res;

        for (int i = 0 ; i < nums.size(); i++ ){
            int cur = nums[i];
            int needed = target - cur;
            if (hmap.contains(needed)){
                res.push_back(i);
                res.push_back(hmap[needed]);
                break;
            }
            hmap[cur] = i;
        }
        return res;
    }
};