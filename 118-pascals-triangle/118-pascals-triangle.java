class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> answer = new ArrayList<List<Integer>>();
        for(int i=0; i<numRows; i++){
            List<Integer> curr = new ArrayList<Integer>();
            if(answer.size()>=1){
                curr.add(0, 1);
                
                for(int j=1; j<i; j++){
                    curr.add(j, answer.get(i-1).get(j-1)+answer.get(i-1).get(j));
                }
                curr.add(1);
            }else{
                curr.add(1);
            }
            answer.add(curr);
        }
        return answer;
    }
}