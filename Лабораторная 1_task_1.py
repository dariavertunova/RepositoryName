numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

#Находим индекс пропущенного элемента
missing_index = numbers.index(None)

#Суммируем все элементы, кроме пропуска
sum_numbers = sum(numbers[:missing_index] + numbers[missing_index+1:])

#Вычисляем количество элементов, включая пропуск
count_numbers = len(numbers)

#Вычисляем среднее арифметическое
average = sum_numbers / count_numbers

#Заменяем пропуск средним арифметическим
numbers[missing_index] = average

print("Измененный список:",numbers)
