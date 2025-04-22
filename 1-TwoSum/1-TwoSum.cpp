// Last updated: 22/04/2025 16:49:43
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res;
        bool etat = false;
        for (int i = 0; i <nums.size(); i++) {
            if (etat == false){
                for(int j =0; j < nums.size(); j++){
                    if(j != i){
                        if (nums[i] + nums[j] == target){
                            res.push_back(i);
                            res.push_back(j);
                            etat = true;
                            break;
                        }
                    }
                }
            }else{
                break;
            }        
        }
        return res;
    }
};