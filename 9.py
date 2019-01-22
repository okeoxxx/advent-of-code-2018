number_of_players = 486
highest_token = 7083300

scores = [0 for p in range(number_of_players)]


board=[0]
i = 1
for n in range(1,highest_token+1):
    if n % 23 == 0:
        i -= 9
        if i < 0:
            i = len(board)+i
        deleted = board.pop(i)
        try:
            scores[n%number_of_players] += n+deleted
            i += 2
            continue
        except IndexError:
            i = 0
            scores[n%number_of_players] += n+deleted
            i += 2
            continue

    if i > len(board):
        i = 1

    board.insert(i,n)
    i += 2
    if n % 10000 == 0:
        print(n)





print(max(scores))
