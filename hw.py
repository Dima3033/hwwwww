import random
size = int(input('Введіть число розміру - '))
begin = int(input('Введіть число початку - '))
end = int(input('Введіть кінцеве число - '))
list_1 = list()
for i in range(size):
    list_1.append(random.randint(begin, end))
for i in range(0, len(list_1)):
    print(f'{list[i]}[{i}]', end=' ')
print()
size2 = int(input('Розмір 2 - '))
begin2 = int(input('початок 2 - '))
end2 = int(input('кінцеве число 2 - '))
list_2 = list()
for i in range(size2):
    list_2.append(random.randint(begin2, end2))
for i in range(0, len(list_2)):
    print(f'{list_2[i]}[{i}]', end=' ')
print()
sum = list_1 + list_2
print(f'Merged list: {sum}')
dup_1 = list(dict.fromkeys(sum))
print(f'List whithout duplicates = {dup_1}')
dup_2 = [x for n, x in enumerate(sum) if x in sum[:n]]
print(f'Duplicates = {dup_2}')
print(f'min - {(min(sum))}')
print(f'max - {(max(sum))}')