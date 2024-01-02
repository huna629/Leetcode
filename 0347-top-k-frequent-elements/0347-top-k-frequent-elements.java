class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> hashMap = new HashMap<Integer, Integer>();
        for(int i:nums){
            if(hashMap.containsKey(i)){
                hashMap.put(i, hashMap.get(i)+1);
            } else {
                hashMap.put(i, 1);
            }
        }

        
        PriorityQueue<int[]> queue = new PriorityQueue<>((a, b) -> Integer.valueOf(b[1]).compareTo(Integer.valueOf(a[1])));
        for(Map.Entry<Integer, Integer> set:hashMap.entrySet()){
            int[] temp = {set.getKey(), set.getValue()};
            queue.offer(temp);
        }
        
        int[] ans = new int[k];
    
        for(int i=0; i<k; i++){
            ans[i] = queue.poll()[0];
        }
        return ans;
    }
}