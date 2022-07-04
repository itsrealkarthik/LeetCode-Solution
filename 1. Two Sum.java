//Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

//soln
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int i=0;i<nums.length-1;i++){
            int diff=target-nums[i];
            for(int j=i+1;j<nums.length;j++){
                if (nums[j]==diff){
                    int fin[]={i,j};
                    return fin;
                }
            }
        }
    return new int[]{0,0};}
}