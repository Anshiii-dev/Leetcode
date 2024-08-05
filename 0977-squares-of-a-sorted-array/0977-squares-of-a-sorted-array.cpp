class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        // Online C++ compiler to run C++ program online
    
    int size=nums.size();
     for(int i=0;i<size;i++){
        nums[i]=nums[i]*nums[i];

     }
     sort(nums.begin(),nums.end());
     return nums;}
};
