# 1 часть. Преобразование введённой последовательности в список

array_list = input("Введите последовательность чисел через пробел:").split()
array_list = list(map(int, array_list))

print(type(array_list))

# 2 часть. Сортировка списка по возрастанию элементов в нем

for i in range(len(array_list)):
    for j in range(len(array_list)-i-1):
        if array_list[j] > array_list[j+1]:
            array_list[j], array_list[j+1] = array_list[j+1], array_list[j]
print(array_list)

# 3 часть. Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.

element = int(input('Введите любое число в рамках последовательности: '))
while element:
    if element not in range(min(array_list) + 1, max(array_list)):
        print('Некорректное число')
        element = int(input('Введите любое число в рамках последовательности: '))
    else:
        break

array_list.append(element)
for i in range(len(array_list)):
    idx_min = i
    for j in range(i, len(array_list)):
        if array_list[j] < array_list[idx_min]:
            idx_min = j
    if i != idx_min:
        array_list[i], array_list[idx_min] = array_list[idx_min], array_list[i]
print(array_list)

def binary_search(array_list, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array_list[middle] == element:
        return middle - 1
    elif element < array_list[middle]:
        return binary_search(array_list, element, left, middle - 1)
    else:
        return binary_search(array_list, element, middle + 1, right)
print(binary_search(array_list, element, 0, len(array_list) - 1))


