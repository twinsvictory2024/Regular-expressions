from models import Peoples
import re


def format_fio(contact_list: list):  # переписываем поля в объекты
    division_list = []
    for object in contact_list:
        division = ' '.join(object[:3]).split(' ')
        object[0], object[1], object[2] = division[0], division[1], division[2] if len(
            division) > 2 else ''
        division_list.append(Peoples(
            object[0], object[1], object[2], object[3], object[4], object[5], object[6]))

    return division_list[1:]


def format_phone(contact_list: list):
    for people in contact_list:
        # чистим номера от символов
        people.phone = re.sub(r'[^\d+]', '', people.phone)
        # проверка добавочного
        match = re.match(
            r'(\+7|8)?(\d{3})(\d{3})(\d{2})(\d{2})(\d{4})?', people.phone)
        if match:
            # Форматируем номер
            if match.group(6):  # Если есть добавочный номер
                people.phone = f"+7({match.group(2)}){match.group(3)}-{match.group(4)}-{
                    match.group(5)} доб.{match.group(6)}"
            else:  # Если добавочного номера нет
                people.phone = f"+7({match.group(2)}){match.group(3)
                                                      }-{match.group(4)}-{match.group(5)}"


def search_duplicate(contact_list: list):
    idx = []

    for idx_1, people_1 in enumerate(contact_list):
        for idx_2, people_2 in enumerate(contact_list):
            # ищем одинаковые фамилию имя и запоминаем индексы
            if (people_1.firstname == people_2.firstname and people_1.lastname == people_2.lastname) and idx_1 != idx_2:
                el = sorted((idx_1, idx_2))
                if not el in idx:
                    idx.append(el)
            # ищем одинаковые тел почту и запоминаем индексы
            if ((people_1.phone == people_2.phone) and (people_1.email == people_2.email)) and idx_1 != idx_2:
                el = sorted((idx_1, idx_2))
                if not el in idx:
                    idx.append(el)
    # слияние дублежей и удаление из списка
    for a in idx[::-1]:
        contact_list[a[0]].copy(contact_list[a[1]])
        contact_list.pop(a[1])

    return contact_list
