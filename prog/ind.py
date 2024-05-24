#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Для своего индивидуального задания
# лабораторной работы 2.23 необходимо реализовать
# вычисление значений в двух функций в отдельных процессах.


from math import cos, fabs, log, pi, sin
from multiprocessing import Process, Queue

EPS = 10e-7


# 11 Вариант
def sum_1(x, queue_obj):

    a = sin(x)
    S, k = a, 2
    # Найти сумму членов ряда.
    while fabs(a) > EPS:
        coef = 2 * k - 1
        a = sin(coef * x) / coef
        S += a
        k += 1

    queue_obj.put(S)


# 12 Вариант
def sum_2(x, queue_obj):

    a = cos(x)
    S, k = a, 2
    # Найти сумму членов ряда.
    while fabs(a) > EPS:
        a = cos(k * x) / k
        S += a
        k += 1

    queue_obj.put(S)


def main():
    queue_obj = Queue()

    pc1 = Process(target=sum_1, args=(pi / 2, queue_obj))
    pc2 = Process(target=sum_2, args=(pi, queue_obj))

    pc1.start()
    pc2.start()

    pc1.join()
    pc2.join()

    sum1, sum2 = queue_obj.get(), queue_obj.get()
    control_value_1 = pi / 4
    control_value_2 = -log(2 * sin(pi / 2))

    print(f"Сумма ряда 1: {round(sum1, 4)}")
    print(f"Контрольное значение ряда 1: {round(control_value_1, 4)}")
    print(f"Проверка: {round(sum1, 4) == round(control_value_1, 4)}")

    print(f"x2 = {pi}")
    print(f"Сумма ряда 2: {round(sum2, 4)}")
    print(f"Контрольное значение ряда 2: {round(control_value_2, 4)}")
    print(f"Проверка: {round(sum2, 4) == round(control_value_2, 4)}")


if __name__ == "__main__":
    main()
