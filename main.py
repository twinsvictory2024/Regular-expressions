from pprint import pprint
from views import format_phone, format_fio, search_duplicate
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    header = contacts_list[0]

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код


contacts_list = format_fio(contacts_list)
format_phone(contacts_list)
search_duplicate(contacts_list)
pprint([a.__str__() for a in contacts_list])

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    contacts_list = [a.make_list() for a in contacts_list]
    contacts_list.insert(0, header)
    datawriter.writerows(contacts_list)
