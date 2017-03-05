from datetime import date
from datetime import datetime
import csv

class Person(object):

    def __init__(self, surname, first_name, birth_date, nickname = None):
        self.surname = surname
        self.first_name = first_name
        if nickname is None:
            self.nickname = surname
        else:
            self.nickname = nickname
        date_format = "%Y-%m-%d"
        datetime_object = datetime.strptime(birth_date, date_format)
        self.birth_date = datetime_object.date()

        #birth_date_chanded = birth_date.replace('.', '-')
        #date_datetime = date.strftime(birth_date_chanded, "%Y-%m-%d")
        #self.birth_date = date_datetime

    def get_age(self):
        today = date.today()
        delta_in_days = today - self.birth_date
        years = delta_in_days.days // 365.25
        return str(int(years))

    def get_fullname(self):
        return self.surname + " " + self.first_name

def find_oldest_person(filename):
    biggest = 0 # возраст
    name = '' # вывести имя
    f = open(filename, 'r') # открыть файл
    f.readline() # пропустить первю строку
    csv_r = csv.reader(f)
    for row, i in csv_r: # для каждой строки в файле
        i.Person(row) # создаем классы
        if row.birth_date > biggest: # определяем наиболший возраст
           biggest = i.birth_date # заносим возраст
           name = Person.get_fullname() # заносим имя
    f.close() # закрыть файл
    return name # вернуть имя