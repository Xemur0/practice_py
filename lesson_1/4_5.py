# Написать программу «Банковский депозит».
# Клиент банка делает депозит на определенный срок.
#
# В зависимости от суммы и срока вклада определяется процентная ставка:
# 1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых,
# 2 и более года — 5 % годовых).

# 10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых,
# 2 и более года – 6.5 % годовых).

# 100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых,
# 2 и более года — 7.5 % годовых).
#
# Проценты начисляются на депозит в конце каждого месяца.
#
# Необходимо написать функцию, в которую будут передаваться параметры:
# сумма вклада и срок вклада (в месяцах), а на выходе возвращать сумму
# вклада на конец срока.


def get_percent(amount, months):
    if months > 24:
        return months

    if months not in [6, 12, 24]:
        return False

    rates = (
        {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5},
        {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5},
        {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5},
    )

    for rate in rates:
        if rate['begin_sum'] <= amount < rate['end_sum']:
            return rate[months]

    return False


def deposit(amount, months):
    percent = get_percent(amount, months)
    if not percent:
        print('6, 12, 24, более 24')

    total = amount
    for month in range(months):
        profit = total * percent / 100 / 12
        total += profit

    return round(total, 2)


print(deposit(10000, 25))


def update_deposit(amount, months, update=0):
    percent = get_percent(amount, months)
    if not percent:
        print('6, 12, 24, более 24')

    total = amount
    for month in range(months):
        profit = total * percent / 100 / 12
        total += profit
        if month != 0 and month != months - 1:
            total += update + update * percent / 100 / 12

    return round(total, 2)


print(update_deposit(10000, 25, 100))
