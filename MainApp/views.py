import pandas as pd

from os import mkdir
from os import error as os_error

from random import choice

from pathlib import Path

from django.shortcuts import render, redirect

from MainApp.forms import T_R_F, D_R_F, S_R_F, B_R_F, C_T_R_F


import psycopg2
from psycopg2.errors import OperationalError, DuplicateDatabase, InvalidSchemaName

BASE_DIR = Path(__file__).resolve().parent.parent

# Первичные функции

def teacher_registration(request):
    form = T_R_F()

    return render(request, "Teacher register.html", {"form": form})

def get_TRF_form(request):
    if request.method == "POST":
       form = T_R_F(request.POST)
       if form.is_valid():
           connection = create_connection("db", "student", "123456", "localhost", "5432")
           query = f"""INSERT INTO data.teachers (name, surname, surname1)
                       VALUES ('{T_R_F.Meta.model.Name}', '{T_R_F.Meta.model.Surname}', '{T_R_F.Meta.model.Surname1}');"""
           executor(connection, query)
           form.save()
           return redirect("http://127.0.0.1:8000")
       return render(request,'Teacher register.html', {'form': form})



def discipline_registration(request):
    form = D_R_F()

    return render(request, "Discipline register.html", {"form": form})

def get_DRF_form(request):
    if request.method == "POST":
       form = D_R_F(request.POST)
       if form.is_valid():
        for copy_checker in Data_container.cabinets:
            if D_R_F.Meta.model.Discipline_name == copy_checker:
                return "Такая дисциплина уже существует!"
        Data_container.cabinets.append(D_R_F.Meta.model.Discipline_name)
        form.save()
        return redirect("http://127.0.0.1:8000")
    return render(request, "Discipline register.html", {"form": form})


def subject_registration(request):
    form = S_R_F()

    return render(request, "Subject register.html", {"form": form})

def get_SRF_form(request):
    if request.method =="POST":
        form = S_R_F(request.POST)
        if form.is_valid():
            for copy_checker in Data_container.subjects:
                if S_R_F.Meta.model.Subject_name == copy_checker:
                    return "Такое оборудование уже существует!"
            Data_container.subjects.append(S_R_F.Meta.model.Subject_name)
            form.save()
            return redirect("http://127.0.0.1:8000")
    return render(request, "Subject register.html", {"form": form})


def building_registration(request):
    form = B_R_F()

    return render(request, "Building register.html", {"form": form})

def get_BRF_form(request):
    if request.method =="POST":
        form = B_R_F(request.POST)
        if form.is_valid():
            for copy_checker in Data_container.buildings:
                if B_R_F.Meta.model.Building_name == copy_checker:
                    return "Такой филиал уже существует!"
            Data_container.buildings.append(B_R_F.Meta.model.Building_name)
            form.save()
            return redirect("http://127.0.0.1:8000")
    return render(request, "Building register.html", {"form": form})


def cabinet_type_registration(request):
    form = C_T_R_F()

    return render(request, "Cabinet type register.html", {"form": form})

def get_CTRF_form(request):
    if request.method =="POST":
        form = C_T_R_F(request.POST)
        if form.is_valid():
            for copy_checker in Data_container.types:
                if C_T_R_F.Meta.model.Cabinet_type_name == copy_checker:
                    return "Такой тип кабинета уже существует!"
            Data_container.types.append(C_T_R_F.Meta.model.Cabinet_type_name)
            form.save()
            return redirect("http://127.0.0.1:8000")
    return render(request, "Cabinet type register.html", {"form": form})


# Вторичные функции - создаются с использованием данных класса Data_container созданных первичными функциями

def cabinets_registration(building: str, new_cabinet_number: int, cab_type: str,
                      containing_subjects: str):  # Ожидает ввода клиентом Кабинета и данных о нём.
    for checker in Data_container.buildings:
        if building == checker:
            for checker1 in Data_container.types:
                if cab_type == checker1:
                    for checker2 in Data_container.subjects:
                        if checker2 == containing_subjects:
                            cab = {"Филиал": building,
                                   "Номер": new_cabinet_number,
                                   "Тип": cab_type,
                                   "Оборудование": containing_subjects}
                            Data_container.cabinets.append(cab)  # В классе Data_container будут содержаться данные о кабинете
                            return cab
                        else:
                            return "Некоторое оборудование не обнаружено!"
            else:
                return "Некоторые данные не обнаружены!"


def descipline_full_info(disciplines: list, *teacher_data: dict, ):
    a = 0
    f_i = {}

    for i in range(len(teacher_data)):
        a += 1
        for q in teacher_data:
            f_i[f"учитель {a}"] = q
    f_i.update(disciplines)
    f_i.update()

    Data_container.full_info_container.append(f_i)
    return f_i


class Data_container: # После внедрения PGSQL будет удалён

    buildings = []

    types = []

    teachers = []

    disciplines = []

    subjects = []

    cabinets = []

    full_info_container = []


# Третичные функции управляют данными вышестоящих функций и класса Data_container


# Создаём директорию для файла (Если он есть, отлавливаем ошибку, не давая программе)
# Прерваться на ней.
# ||
# \/

def excel_maker():
    try:
        mkdir("C:/Users/timiv/OneDrive/Рабочий стол/Papka")
    except os_error as err:
        print(err)

    g1 = list
    g2 = list
    g3 = list
    g4 = list

    df = pd.DataFrame({
        "20CА-22К": [g1],
        "22ИС-22К": [g2],
        "22/1ИС-22К": [g3],
        "22/1ИСд": [g4],
    })

    df.to_excel[BASE_DIR / 'sample.xlsx']


# -------------------------------------------------------- #
# ------------ Функции для работы с tempplate ------------ #
# -------------------------------------------------------- #

def create_connection(db_name, db_user, db_password, db_host, db_port):
        connection = None
        try:
            connection = psycopg2.connect(
                database=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port,
            )
            print("Connection to PostgreSQL DB successful")
        except OperationalError as e:
            print(f"The error '{e}' occurred")
        return connection

def main_page(request):

    return render(request, "htmldoc.html")

def executor(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

def db_create_button(request):
    connection = create_connection("db", "student", "123456", "localhost", "5432")
    try:
        scq = """CREATE SCHEMA IF NOT EXISTS data;"""
        executor(connection, scq)
        ttcq = """CREATE TABLE IF NOT EXISTS data.teachers
        (name varchar(96) NOT NULL,
        surname varchar(96) NOT NULL,
        surname1 varchar(96) NOT NULL);"""        
        executor(connection, ttcq)
        return render(request, "htmldoc.html")
    except DuplicateDatabase as dberr:
        return render(request, "htmldoc.html", {"DDBerr": dberr})

def db_drop_button(request):
    try:
        connection = create_connection("db", "student", "123456", "localhost", "5432")
        drop_database_query = "DROP SCHEMA data CASCADE;"
        ddb = executor(connection, drop_database_query)
        return render(request, "htmldoc.html", {"ddb": ddb})
    except InvalidSchemaName as dberr:
        return render(request, "htmldoc.html", {"ICNerr": dberr})