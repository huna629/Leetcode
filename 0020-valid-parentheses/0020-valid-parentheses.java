class Solution {
    
    private HashMap<Character, Character> mappings;
    
    public Solution(){
        this.mappings = new HashMap<Character, Character>();
        this.mappings.put(')', '(');
        this.mappings.put(']', '[');
        this.mappings.put('}', '{');
    }
    
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for(int i=0; i<s.length(); i++){
            char curr = s.charAt(i);
            if(this.mappings.containsKey(curr)){
                char topElement = stack.empty() ? '#' : stack.pop();
                if(topElement!=this.mappings.get(curr)){
                    return false;
                }
            } else{
                stack.push(curr);
            }
        }
        return stack.isEmpty();
    }
}