# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, separator=','):

    # Разделяем строки на списки участников
    participants_group1 = set(group1.split(separator))
    participants_group2 = set(group2.split(separator))

    # Находим общих участников
    common_participants = participants_group1.intersection(participants_group2)

    # Возвращаем отсортированный список общих участников
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

result = find_common_participants(participants_first_group, participants_second_group, separator='|')
print(result)