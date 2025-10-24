
# №1

enter = input('Введите текст' )
spisok_slov = list(enter.split())
reverse_spisok_slov = []
stroka1 = ''
stroka2 = ''

for x in reversed(range(len(spisok_slov))):
    reverse_spisok_slov.append(spisok_slov[x])

for y in range(len(reverse_spisok_slov)):
    stroka1 += f'{str(reverse_spisok_slov[y])} '

for z in reversed(range(len(list(enter)))):
    stroka2 += list(enter)[z]

print(f'{enter} - {stroka1}')
print(f'{enter} - {stroka2}')




























