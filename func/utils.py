import json
import datetime


def load_operations_list(path):
    """
   Функция загружает данные из файла .json
   """
    with open(path, 'r', encoding='utf-8') as file:
        operations_list = json.load(file)
    return operations_list


def operation_data(data):
    """
   Функция возвращает только выполненные транзакции
   """
    data_operation = []
    for operation in data:
        if operation.get('state') == "EXECUTED":
            data_operation.append(operation)
        elif operation.get('state') == "CANCELED":
            continue
    return data_operation


def sorted_operations(data):
    """Функция возвращает список словарей по дате
    """
    sorted_operation = sorted(operation_data(data), key=lambda x: x['date'], reverse=True)
    return sorted_operation


def format_date(data):
    """Функция возвращает дату перевода в формате ДД.ММ.ГГГГ
    """
    date = datetime.datetime.strptime(data['date'], '%Y-%m-%dT%H:%M:%S.%f')
    return date.strftime('%d.%m.%Y')


def format_number(number):
    """Функция шифрует номер карты и номер счета **
    """
    if len(number) == 16:
        return f'{number[:4]} {number[4:6]}** **** {number[-4:]}'
    elif len(number) == 20:
        return f'**{number[-4:]}'


def last_operations(sorted_list):
    operation = ''
    for i in sorted_list:
        date = format_date(i)
        description = i['description']
        currency = i['operationAmount']["currency"]["name"]
        amount = i['operationAmount']["amount"]
        to_name = i['to'].split()[0]
        to_number = i['to'].split()[-1]
        if i.get('from') is not None:
            from_name = ' '.join(i['from'].split()[:-1])
            from_number = i['from'].split()[-1]
            operation += f'{date} {description}\n{from_name} {format_number(from_number)} -> {to_name} {format_number(to_number)}\n{amount} {currency}\n----------------------\n'
        else:
            from_name = "Unknown"
            operation += f'{date} {description}\n{from_name} -> {to_name} {format_number(to_number)}\n{amount} {currency}\n---------------------\n'

    return operation







