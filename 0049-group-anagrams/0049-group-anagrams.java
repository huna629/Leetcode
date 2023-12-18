class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        
        for(String s: strs){
            char[] arr = s.toCharArray();
            Arrays.sort(arr);
            String temp = new String(arr);
            if(!map.containsKey(temp)){
                map.put(temp, new ArrayList<String>());
            }
            map.get(temp).add(s);
        }
        
        return new ArrayList<>(map.values());
    }
}