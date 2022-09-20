class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()==0 && t.length()==0) return true;
        if(s.length()!=t.length()){ return false; }
        /**
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
        **/
        HashMap<Character, Integer> mapS = new HashMap<Character, Integer>();
        for(int i=0; i<s.length(); i++){
            if(mapS.containsKey(s.charAt(i))){
                mapS.put(s.charAt(i), mapS.get(s.charAt(i))+1);
            }else{
                mapS.put(s.charAt(i), 1);
            }
        }
        
        HashMap<Character, Integer> mapT = new HashMap<Character, Integer>();
        for(int i=0; i<t.length(); i++){
            if(mapT.containsKey(t.charAt(i))){
                mapT.put(t.charAt(i), mapT.get(t.charAt(i))+1);
            }else{
                mapT.put(t.charAt(i), 1);
            }
        }
        return mapS.equals(mapT);
    }
}