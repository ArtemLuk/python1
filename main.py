
#Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

'''
n = int(input('Введите число: '))
print(f'Число цифр равно: {int(n%10+n/10%10+n/100%10)}')
'''

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество
# журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

'''
n = int(input('Введите число журавликов: '))
print(f'Петя и Сережа сделали по {n/6:.0f} журавликов')
print(f'А Катя сделала {n/3*2:.0f} журавликов')
'''

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет 
#с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна 
#сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать 
# программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

'''
n = int(input('Введите число билета: '))
a=int(n/100000%10)
b=int(n/10000%10)
c=int(n/1000%10)
d=int(n/100%10)
e=int(n/10%10)
f=int(n%10)
if a+b+c == d+e+f:
    print('Ура! Вам попался счастливый билетик!')
else:
    print('В следующий раз повезет обязательно')
'''
# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается 
# сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

'''
n=int(input('Введите число n: '))
m=int(input('Введите число m: '))
k=int(input('Введите число k: '))
if k<n and k<m:
            print('NO')
elif k%n==0 or k%m==0:
    print('yes')
else:
    if (m*n-k)%k==0 and m*n%k==0:
        print('yes')
'''
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# n=int(input('Введите число монеток n: '))
# count_0 = 0
# count_1 = 0
# for i in range(n):
#     i = int(input())
#     if i ==0:
#         count_0 +=1
#     elif i ==1:
#         count_1 +=1
#     else:
#         input('Такой монетки не существует, конец игры')
#         break
# if count_0 < count_1:
#     input(f'Нужно перевернуть {count_0} монеток')
# if count_0 > count_1:
#     input(f'Нужно перевернуть {count_1} монеток')

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# S = int(input('Введите сумму чисел: '))
# P = int(input('Введите произведение чисел: '))
# for i in range(S):
#     for j in range(P):
#         if S == i + j and P == i * j:
#             print(f'Числа: {i, j}')
            
# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# N = int(input('Введите чило N: '))
# i=1
# while i**2 < N:
#     print(i**2)
#     i +=1