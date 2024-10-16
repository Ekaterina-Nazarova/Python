numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
index = numbers.index(None)
sum_ = sum(numbers[:index]) + sum(numbers[(index+1):])
count_of_numbers = len(numbers)
average = sum_/count_of_numbers
numbers[index] = average
print("Измененный список:", numbers)
