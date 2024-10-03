import scipy.integrate as integrate

# Ввод значений a и b
a = float(input("Введите значение a (границы отрезка [-a, a]): "))
b = float(input("Введите значение b (для уравнения x + y > b): "))

# Функция для вычисления верхней границы y = a - (b - x)
def integrand(x):
    return a - (b - x)

# Вычисление площади благоприятной области
area, _ = integrate.quad(integrand, -a, a)

# Общая площадь квадрата
total_area = (2 * a) ** 2  # Площадь квадрата 2a x 2a

# Вероятность
probability = area / total_area

# Результат
print(f"Площадь благоприятной области: {area:.2f}")
print(f"Общая площадь: {total_area}")
print(f"Вероятность того, что x + y > {b}: {probability:.3f}")
