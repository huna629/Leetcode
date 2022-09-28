class Solution {
   
    public List<List<Integer>> generate(int numRows) {
        
        /**
        if(numsRows<=1){
            answer.add(Arrays.asList(1));
            return answer;
        }else{
            List<Integer> list = new ArrayList<List<Integer>>();
            
        }
        **/
        List<List<Integer>> answer = new ArrayList<List<Integer>>();
        
        for(int i=0; i<numRows; i++){
            List<Integer> curr = new ArrayList<Integer>();
                for(int j=0; j<i+1; j++){
                    if(j==0 || j==i){
                        curr.add(1);
                    }else{  
                        curr.add(answer.get(i-1).get(j-1)+answer.get(i-1).get(j));
                    }
                }
            answer.add(curr);
        }
        return answer;
        
    }
}