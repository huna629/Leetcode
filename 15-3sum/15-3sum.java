class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> ans = new HashSet<>();
        if(nums.length<3){
            return new ArrayList<>(ans);
        }

        Arrays.sort(nums);
        
        for(int i=0; i<nums.length-2; i++){
            
            int sum = 0;
            int j=i+1;
            int k=nums.length-1;
            while(j<k){
                sum=nums[i]+nums[j]+nums[k];
                if(sum==0){
                    
                    ans.add(new ArrayList<>(Arrays.asList(nums[i], nums[j], nums[k])));
                    j++;
                    k--;
                }else if(sum>0){
                    k--;
                }else if(sum<0){
                    j++;
                }
            }
        }
        return new ArrayList<>(ans);
    }
}