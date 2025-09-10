class Solution {
public:
    int thirdMax(vector<int>& nums) {
        sort(nums.begin(),nums.end(), greater<int>());
        int c = 1;
        int pre = nums[0];
        for(int index = 1; index < nums.size(); ++index){
            if (nums[index] != pre){
                c += 1;
                pre = nums[index];
            }
            if (c == 3){
                return nums[index];
            }    
        }
        return nums[0];
    }
};