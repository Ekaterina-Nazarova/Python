def find_common_participants(str_1, str_2, separator=","):
    participants1 = str_1.split(separator)
    participants2 = str_2.split(separator)
    intersection_participants = list(set(participants1).intersection(participants2))
    intersection_participants.sort()
    return intersection_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common = find_common_participants(participants_first_group, participants_second_group, separator="|")
print("Общие участники:", common)
