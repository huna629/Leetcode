class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()==0 && t.length()==0) return true;
        if(s.length()!=t.length()){ return false; }
        HashMap<Character, Integer> maps = new HashMap<Character, Integer>();
        for(int i=0; i<s.length(); i++){
            if(maps.containsKey(s.charAt(i))){
                maps.put(s.charAt(i), maps.get(s.charAt(i))+1);
            }else{
                maps.put(s.charAt(i), 1);
            }
        }
        
        for(int j=0; j<t.length(); j++){
            if(maps.containsKey(t.charAt(j)) && maps.get(t.charAt(j))>0){
                maps.put(t.charAt(j), maps.get(t.charAt(j))-1);
            }else{
                return false;
            }
        }
        return true;
    }
}