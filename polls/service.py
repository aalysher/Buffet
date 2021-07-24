from polls.models import User, Pin, Buffet


def create_pin(phone, obj):
    """Создает новый пин по последним 6 цифрам номера телефона"""
    number = 0
    pin = int(phone[-6:])
    while obj.objects.filter(pin=pin + number):
        number += 1
    return str(pin + number).zfill(6)


def get_total_sum(validate_data):
    """Получает итоговую сумму"""
    total_sum = 0
    for i in validate_data['basket']:
        buffet = Buffet.objects.get(pk=i['buffet'].id)
        total_sum += int(i['amount']) * buffet.price
    return total_sum


def get_status(validated_data, total_sum):
    """Получение статуса"""
    if total_sum <= validated_data['payment']:
        return 1
    return 2


def get_debt_and_change(validated_data, total_sum):
    """Получить долг"""
    debt_sum = 0
    change = 0
    if total_sum >= validated_data['payment']:
        debt_sum = total_sum - validated_data['payment']
    if debt_sum == 0:
        change = abs(validated_data['payment'] - total_sum)
    return debt_sum, change
