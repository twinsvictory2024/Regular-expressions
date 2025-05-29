class Peoples():
    def __init__(self, lastname, firstname, surname, organization, position, phone, email):
        self.lastname = lastname
        self.firstname = firstname
        self.surname = surname
        self.organization = organization
        self.position = position
        self.phone = phone
        self.email = email

    def __str__(self):
        return (f"Фамилия: {self.lastname}, "
                f"Имя: {self.firstname}, "
                f"Отчество: {self.surname}, "
                f"Организация: {self.organization}, "
                f"Должность: {self.position}, "
                f"Телефон: {self.phone}, "
                f"Email: {self.email}")

    # метод слияния объектов
    def copy(self, object):
        self.lastname += object.lastname if object.lastname != self.lastname else ''
        self.firstname += object.firstname if object.firstname != self.firstname else ''
        self.surname += object.surname if object.surname != self.surname else ''
        self.organization += object.organization if not self.organization or self.organization != object.organization else ''
        self.position += object.position if not self.position or self.position != object.position else ''
        self.phone += object.phone if not self.phone or self.phone != object.phone else ''
        self.email += object.email if not self.email or self.email != object.email else ''
        return self

    # метод объект в список
    def make_list(self):
        return [self.lastname, self.firstname, self.surname, self.organization, self.position, self.phone, self.email]
