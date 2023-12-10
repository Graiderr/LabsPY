money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

count = 0
while True:
    money_capital += salary - spend # изменение бюджета за месяц
    spend *= 1 + increase # увеличение расходов
    if money_capital >= 0: # если деньги еще остались
        count += 1
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", count)
