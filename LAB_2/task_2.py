salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
dolg = 0
for i in range(months):
    dolg += (salary - spend)
    spend *= (1+increase)
podushka = dolg * -1
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(podushka))
