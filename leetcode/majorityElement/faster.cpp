class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
         int count1 = 0;
        int element1,element2;
        int count2=0;
        for(int i =0;i<nums.size();i++)
        {
           if(element1==nums[i]){
               count1=count1+1;
           }
            else if(element2==nums[i]){
                count2=count2+1;
            }
            else if(count1==0){
                element1=nums[i];
                count1=count1+1;
            }
            else if(count2==0){
                element2=nums[i];
                count2=count2+1;
            }
            else{
                count1--;
                count2--;
            }
            
        }
        int val1=0;
        int val2=0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]==element1){
                val1++;
            }
            else if(nums[i]==element2){
                val2++;
            }
        }
       int n=nums.size()/3;
        vector<int>v;
        if(val1>n){
            v.push_back(element1);
        }
        if(val2>n){
            v.push_back(element2);
        }
        return v;
    }
};