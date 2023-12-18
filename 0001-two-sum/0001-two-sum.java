class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        for(int i=0; i<nums.length; i++){
            int find = target-nums[i];
            if(hashMap.containsKey(find)){
                int[] ans = {i, hashMap.get(find)};
                return ans;
            }
            hashMap.put(nums[i], i);
        }
        return null;
    }
}