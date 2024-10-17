def check_pos(x, y):
    pos = [-1, 0, 1]
    if board[x][y] != "*": 
        for i in pos:
            for j in pos:
                if i != 0 or j != 0:
                    if board[x+i][y+j] == "*":
                        board[x][y] += 1
                        
answer = input()
k = int(input())
l = []
for i in range(k):
    l.append(list(input()))
    l[i].remove(" ")
# print(l)
    
m = int(answer.split(" ")[0])
n = int(answer.split(" ")[1])
board = []
if 1 <= m and n <= 100:
    if 1 <= k <= n*m:
        for i in range(m):
            board.append([])
            for j in range(n):
                board[i].append(0)
        #print(board)
        for i in range(len(l)):
            row = int(l[i][0])
            col = int(l[i][1])
            board[row - 1][col - 1] = "*"
        for i in range(m):
            for j in range(n):
                check_pos(i - 1 , j - 1)
print(board)