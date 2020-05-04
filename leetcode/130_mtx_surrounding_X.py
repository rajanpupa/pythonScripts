# 130: surrounding regions
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
# Example:
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:
# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. 
# Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
# Two cells are connected if they are adjacent cells connected horizontally or vertically.

from typing import List
class Solution:
    def has_connection(self, board, s, i, j)->bool:
        print(i,j)
        if i==0 or i==len(board)-1: return True
        if j==0 or j==len(board[0])-1: return True
        
        if  (i+1,j ) in s: return True
        if (i-1, j) in s: return True
        if (i, j+1) in s: return True
        if (i, j-1) in s: return True
        print('False', s)
        return False
    
    def solve(self, board: List[List[str]]) -> None:
        # create a set of points that should not be flipped
        s = set() # points which are O
        i = 0
        j = 0
        layer = 0
        while layer <= len(board)/2:
            # go right
            while j < len(board[0])-layer:
                if board[i][j] == 'O':
                    if self.has_connection(board, s, i, j):
                        s.add((i,j))
                    else:
                        board[i][j] = 'X'
                j += 1    
            j -= 1
            # go down
            while i < len(board)-layer:
                if board[i][j] == 'O':
                    if self.has_connection(board, s, i, j):
                        s.add((i,j))
                    else:
                        board[i][j] = 'X'
                i += 1    
            i-=1
            # go left
            while j >= layer:
                if board[i][j] == 'O':
                    if self.has_connection(board, s, i, j):
                        s.add((i,j))
                    else:
                        board[i][j] = 'X'
                j -= 1  
            # j+=1
            # go up
            while i >= layer:
                if board[i][j] == 'O':
                    if self.has_connection(board, s, i, j):
                        s.add((i,j))
                    else:
                        board[i][j] = 'X'
                i -= 1  
            # i += 1    
            layer += 1
            i += 1
            j += 1

def print_matrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j],  end =" ")
        print()

mat = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","O","X"]]
s = Solution()    
s.solve(mat)

print_matrix(mat)