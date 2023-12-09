list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

center = len(list_players) // 2 # номер центральной позиции
team_one = list_players[:center]
team_two = list_players[center:]

print(team_one)
print(team_two)
