from collections import defaultdict
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        move_X = [0]*9
        move_O = [0]*9
             
        def check(arr):
            return (arr[0]==arr[1]==arr[2]==1 or
                    arr[3]==arr[4]==arr[5]==1 or
                    arr[6]==arr[7]==arr[8]==1 or
                    arr[0]==arr[3]==arr[6]==1 or
                    arr[1]==arr[4]==arr[7]==1 or
                    arr[2]==arr[5]==arr[8]==1 or
                    arr[0]==arr[4]==arr[8]==1 or
                    arr[2]==arr[4]==arr[6]==1)
   
        for i in range(0, len(moves)):
            r, c = moves[i]
            if i%2==0:
                move_X[r*3+c]=1
                if i>=4 and check(move_X):
                    return "A"
            else:
                move_O[r*3+c]=1
                if i>=4 and check(move_O): 
                    return "B"
            print(move_X, move_O)
        
        if len(moves)<9: return "Pending"
            
        return "Draw"
