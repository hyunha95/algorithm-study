board = input()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

print(-1 if board.count("X") > 0 else board)
