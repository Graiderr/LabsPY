def find_common_participants(participants_group_one, participants_group_two, list_delimeter=','):
    participants_group_one = set(participants_group_one.split(list_delimeter))
    participants_group_two = set(participants_group_two.split(list_delimeter))
    participants = list(participants_group_one.intersection(participants_group_two))
    participants.sort()
    return participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))
