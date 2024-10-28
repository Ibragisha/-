def luhn_algorithm(card_number):
    card_number = card_number.replace(" ", "")
    reversed_digits = card_number[::-1]
    total_sum = 0
    for i, digit in enumerate(reversed_digits):
        num = int(digit)
        if i % 2 == 1:
            num *= 2
            if num > 9:
                num = num - 9
        total_sum += num
    return total_sum % 10 == 0
card_number = '4799 2739 8713 6272'
if luhn_algorithm(card_number):
    print(f"Номер карты {card_number} корректен.")
else:
    print(f"Номер карты {card_number} некорректен.")