class Solution(object):
    def validTicTacToe(self, board):
        #think of the general cases that would return false since it would break mechanics of the game
        #ie there can't be more O's than X's because X always goes first
        #return false if there's more o's than x's 
        #return false if there's 2 more x's than o's
        countX = 0
        countO = 0
        #checks each individual char in the string for X or O and adds to respective count
        for i in range(3):
            for j in board[i]:
                if j == 'X':
                    countX+= 1
                elif j == "O":
                    countO+=1
        if countO > countX or countX - countO > 1:
            return False

        #return false if both X and O wins

        #check for rows wins
        winX = 0
        winO = 0
        for i in range(3):
            if board[i] == "XXX":
                winX += 1
            elif board[i] == "OOO":
                winO += 1
        #check for column wins, the i variable adjusts the column and the row var is constant
        for i in range(3):
            if board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "X":
                winX += 1
            if board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O":
                winO += 1
        #check for diagonals, two possible positions for X and O each
        if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
                winX += 1
        if board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O":
                winO += 1
        if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
                winO += 1
        if board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X":
                winX += 1
        #O can't have more than 1 three in a row
        if winO > 1:
            return False
        #X can't have more than 2 three in a row
        if winX > 2:
            return False
        #can't both win
        if winX and winO:
            return False
        #if X wins, then xCount must be higher than O count 
        if winX and countX <= countO:
            return False
        #if O wins, then oCount must be equal to X count
        if winO and countX != countO:
            return False
        return True
              



        """
        :type board: List[str]
        :rtype: bool
        """