# --------------------------------------ДЗ к сенимару №2--------------------------------------------------------------------
#Задача №1. Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр.

# a = float(input("Введите число "))
# string_a = str(a) 
# string_a = string_a.replace('.', '') 
# list_a = list(string_a) 
# list_num = map(int, list_a) 
# sumnum = sum(list_num, 0)    
# print(sumnum)

#Задача №2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

# def Fact(n):    
#     f = 1
#     for i in range(1, n+1):
#         f = f * i
#         print (f,end=',')

# n = int(input("Введите N "))
# Fact(n)

#Задача №3. Задайте список из n чисел последовательности (1 + 1/n)^n 
# и выведите на экран их сумму.

# def Seq(n):
#     list_n = [round((1 + 1 / i)**i, 2) for i in range (1, n + 1)]
#     return list_n

# n = int(input("Введите N = "))
# print(Seq(n))  
# print(f"Сумма {round(sum(Seq(n)), 2)}")

#Задача №4. Задайте список из N элементов, заполненных числами
# из промежутка [-N, N]. Найдите произведение элементов
# на указанных позициях. Позиции вводятся с клавиатуры.

# from random import randint
# n = int(input("Введите N "))
# list_n = [randint(-n, n) for i in range(1, n+1)]
# print(list_n)
# x = int(input("Введите позицию 1 элемента: "))
# y = int(input("Введите позицию 2 элемента: "))
# print(f'Произведение равно: {list_n[x - 1] * list_n[y - 1]}')

# Задача №5. Реализуйте алгоритм перемешивания списка.

# from random import randint

# def MixList(list_in):
#     mix_list = list_in[:]
#     for i in range(len(mix_list)):
#         index_rand = randint(0, len(mix_list) - 1)
#         temp = mix_list[i]
#         mix_list[i] = mix_list[index_rand]
#         mix_list[index_rand] = temp
#     return mix_list

# n = int(input("Введите N "))

# list_n = [i for i in range(1, n+1)]
# print("Начальный список: ")
# print(list_n)
# print("Перемешанный список: ")
# print(MixList(list_n))


