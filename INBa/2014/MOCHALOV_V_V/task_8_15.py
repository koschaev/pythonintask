﻿# -*- coding: UTF-8 -*-
# Задача 8. Вариант 15.
# 
# Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.
# Mochalov V. V.
# 14.05.2016

import random
WORDS=("питон","анаграмма","простая","сложная","ответ","подстаканник","абсолютный","честность",
       "авторитетный","мнение", "поступить","академия", "оранжевый","апельсин", "громкий","аплодисменты",
       "цирк","арена", "приятный","аромат", "атака", "благоприятный","атмосфера", "старинный","балкон",
       "бархатный","скатерть", "играть","баскетбол", "безвкусный","конфета", "беречь","имущество", "беседовать",
       "профессия", "размешиват","бетон", "разглядывать", "бинокль", "благородный", "поступок", "прочитать","брошюра")
word=random.choice(WORDS)
correct=word
jumble=""
k=-1
j=""
p=1000
while word:
    position=random.randrange(len(word))
    jumble+=word[position]
    word=word[:position]+word[(position+1):]
print("Добро пожаловатив игру 'Анаграммы'!",
      "\nНадо пререставить буквы так, чтобы получилось слово.\n(Для выхода нажмите Enter, не вводя своей версии.)")
print("Вот анаграмма: ", jumble)
guess=input("\nПопробуйте отгадать слово: ")
while guess!=correct and guess!="":
    help=input("К сожалению, вы неправы. Хотите получить подсказку (напишите 'да')?")
    if help=="да":
        if k<=(len(correct)-2):
         k=k+1
         j=j+correct[k]
         print (j)
         p=p-k
        else:
         print("Превышено максимальное число подсказок")
    p=p-1
    guess=input("Попробуйте еще раз: ")
if guess==correct:
    print("Вы угадали!!!\n")
print("Спасибо за игру!!! Вы набрали ", p," очков.")
input("\n\nНажмите Enter, чтобы выйти.")