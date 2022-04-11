# возвращает все словари в списке
def dicts_in_list(l: list):
    # пустой список
    dicts = []
    # перебираем всё в списке
    for item in l:
        # если это словарь, добавляем в список
        if isinstance(item, dict):
            dicts.append(item)
        # если это список, то рекурсия, результат соединяем со словарем
        elif isinstance(item, list):
            dicts = dicts + dicts_in_list(item)
    # возвращаем список словарей внутри списка
    return dicts


# глубина словаря
def dict_len(mydict, count=0):
    # список глубин ветвей
    branches = []
    # каждый ключ в словаре
    for key in mydict:
        # если это словарь
        if isinstance(mydict[key], dict):
            # добавляем ветку со значением 1
            branches.append(1)
            # рекурсия
            count = dict_len(mydict[key], count)
            # добавляем значение в список
            branches[-1] += count
        # если это список
        elif isinstance(mydict[key], list):
            # перебираем словари в списке
            for item in dicts_in_list(mydict[key]):
                # каждый - новая ветвь
                branches.append(1)
                count = dict_len(item, count)
                branches[-1] += count
    # если нет ветвей, то длина 0, 1 прибавили при добавлении значения в список
    if not branches:
        count = 0
    else:
        # если есть ветви, берем максимальную
        count = max(branches)
    # возвращаем максимальную ветвь
    return count
