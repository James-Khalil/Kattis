correct = (
    ("1", "1", "1", "1", "1"),
    ("0", "1", "1", "1", "1"),
    ("0", "0", " ", "1", "1"),
    ("0", "0", "0", "0", "1"),
    ("0", "0", "0", "0", "0")
)

def findspots(x, y):
    spotlist = []
    for dx, dy in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 5 and 0 <= new_y < 5:
            spotlist.append((new_x, new_y))
    return spotlist

def findBoards(queue, turn):
    boardList = []
    for board, x, y in queue:
        for spot in findspots(x, y):
            new_board = [list(row) for row in board]
            new_board[x][y] = new_board[spot[0]][spot[1]]
            new_board[spot[0]][spot[1]] = " "
            new_board_tuple = tuple(tuple(row) for row in new_board)
            if new_board_tuple not in visited:
                visited[new_board_tuple] = turn
                boardList.append((new_board_tuple, spot[0], spot[1]))
    return boardList

def BFS(queue):
    turn = 0
    while queue:
        turn += 1
        if turn > 10:
            return
        queue = findBoards(queue, turn)

queue = []
queue.append([correct, 2, 2])
visited = {}
visited[correct] = 0
BFS(queue)
cases = int(input())
for _ in range(cases):
    count = 0
    board = []
    for i in range(5):
        line = input()
        board.append(tuple(line))
    
    if(tuple(board) in visited):
        print("Solvable in " + str(visited[tuple(board)]) + " move(s).")
    else:
        print("Unsolvable in less than 11 move(s).")