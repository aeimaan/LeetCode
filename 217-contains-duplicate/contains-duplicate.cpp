class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::set<int> seen = {};
        bool duplicate_found = false;
        for (int num: nums){
            if (seen.contains(num)){
                duplicate_found = true;
                break;
            }
            seen.insert(num);
        }
        return duplicate_found;
    }
};