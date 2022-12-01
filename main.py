baza_stavka = 30
region = input('Вы проживаете на Дальнем Востоке? (да/нет) :'). lower()
if (region == ('да')):
  print('Ваша базовая ставка ровна 2%')
else:
  print ('Ваша базовая ставка ровна: ',baza_stavka,'%')
  if (region == ('нет')):
   print('Давайте посчитаем ваши остальные скидки')
  deti = int(input('Сколько у вас детей? '))
  if deti > 3:
    baza_stavka = baza_stavka - 2
    print('Ваша базовая ставка ровна',baza_stavka,'%')
  else:
    print('Ваша базовая ставка ровна',baza_stavka,'%')
  salary = input('Есть ли у вас зарплатный проект в нашем банке? (да/нет)')
  if salary == 'да':
    baza_stavka = baza_stavka - 0.5
    print ('Ваша базовая ставка ровна',baza_stavka,'%')
  else:
    print('Ваша базовая ставка ровна',baza_stavka,'%')
  strahovka = input('Хотите ли вы оформить страховку в нашем банке? (да/нет)')
  if strahovka =='да':
    baza_stavka = baza_stavka - 1.5
    print('Ваша базовая ставка ровна',baza_stavka,'%')
  else:
    print('Ваша базовая ставка ровна',baza_stavka,'%')

month = input('Введите ваш месяц рождения: '). lower()
day = int(input ('Введите ваш день рождения: '))
if day > 31:
  print('Вы ввели не верное число')
elif ((20 <= day <= 31 and month == 'март') or (1 <= day <= 20 and month == 'апрель')):
  print('Вы овен')
elif ((21 <= day <= 30 and month == 'апрель') or (1 <= day <= 21 and month == 'май')):
  print('Вы телец')
elif ((22 <= day <= 31 and month == 'май') or (1 <= day <= 21 and month == 'июнь')):
  print('Вы близнецы')
elif ((22 <= day <= 30 and month == 'июнь') or (1 <= day <= 23 and month == 'июль')):
  print('Вы рак')
elif ((24 <= day <= 31 and month == 'июль') or (1 <= day <= 23 and month == 'август')):
  print('Вы лев')
elif ((24 <= day <= 31 and month == 'август') or (1 <= day <= 23 and month == 'сентябрь')):
  print('Вы дева')
elif ((24 <= day <= 30 and month == 'сентябрь') or (1 <= day <= 23 and month == 'октябрь')):
  print('Вы весы')
elif ((24 <= day <= 31 and month == 'октябрь') or (1 <= day <= 22 and month == 'ноябрь')):
  print('Вы скорпион')
elif ((23 <= day <= 30 and month == 'ноябрь') or (1 <= day <= 21 and month == 'декабрь')):
  print('Вы стрелец')
elif ((22 <= day <= 31 and month == 'декабрь') or (1 <= day <= 20 and month == 'январь')):
  print('Вы козерог')
elif ((21 <= day <= 31 and month == 'январь') or (1 <= day <= 19 and month == 'февраль')):
  print('Вы водолей')
elif ((20 <= day <= 28 and month == 'февраль') or (1 <= day <= 20 and month == 'апрель')):
  print('Вы рыбы')
