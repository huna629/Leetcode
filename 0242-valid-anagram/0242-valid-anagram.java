class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()){ return false; }
        HashMap<Character, Integer> hashMap = new HashMap<>();
        char[] arr_s = s.toCharArray();
        char[] arr_t = t.toCharArray();
        
        for (char ch : arr_s) {
            hashMap.put(ch, hashMap.getOrDefault(ch, 0) + 1);
        }
        
        for(char ch:arr_t){
            if(!hashMap.containsKey(ch) || hashMap.get(ch)==0){
                return false;
            }
            hashMap.put(ch, hashMap.get(ch)-1);
        }
        return true;
    }
}