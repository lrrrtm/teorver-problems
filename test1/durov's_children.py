def bayes_theorem(n, k):
    # Вероятность P(A|B_k) = k / n
    p_A_given_Bk = k / n

    # Равномерное распределение вероятности для P(B_k) = 1 / (n + 1)
    p_Bk = 1 / (n + 1)

    # Общая вероятность P(A) = sum((k / n) * (1 / (n + 1))) для всех k от 0 до n
    p_A = sum((k / n) * (1 / (n + 1)) for k in range(n + 1))

    # Используем формулу Байеса для нахождения P(B_k|A)
    p_Bk_given_A = (p_A_given_Bk * p_Bk) / p_A

    return p_Bk_given_A

# Пример ввода данных
n = int(input("Введите количество детей в группе n: "))
k = int(input("Введите количество биологических детей основателя k: "))

# Вывод результата
result = bayes_theorem(n, k)
print(f"Условная вероятность P(B_{k}|A) равна приблизительно {result:.5f}")
