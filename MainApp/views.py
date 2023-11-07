import pandas as pd

from os import mkdir
from os import error as os_error

from random import choice

from pathlib import Path

from django.shortcuts import render, redirect

from MainApp.forms import T_R_F, D_R_F, E_R_F, B_R_F, C_T_R_F


import psycopg2
from psycopg2.errors import OperationalError, DuplicateDatabase, InvalidSchemaName, IntegrityError

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
           query = f"""INSERT INTO data.teachers (teacher_name, surname, surname1)
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
            try:
                connection = create_connection("db", "student", "123456", "localhost", "5432")
                query = f"""INSERT INTO data.disciplines (discipline_names)
                            VALUES ('{D_R_F.Meta.model.Discipline_name}')"""
                executor(connection, query)
                form.save()
                return redirect("http://127.0.0.1:8000")
            except IntegrityError as intgrerr:
                return intgrerr,
    return render(request, "Discipline register.html", {"form": form})


def equipment_registration(request):
    form = E_R_F()

    return render(request, "Equipment register.html", {"form": form})

def get_ERF_form(request):
    if request.method =="POST":
        form = E_R_F(request.POST)
        if form.is_valid():
            try:
                connection = create_connection("db", "student", "123456", "localhost", "5432")
                query = f"""INSERT INTO data.subjects (subject_names)
                            VALUES ('{E_R_F.Meta.model.Subject_name}');"""
                executor(connection, query)
                form.save()
                return redirect("http://127.0.0.1:8000")
            except IntegrityError as intgrerr:
                return intgrerr
    return render(request, "Equipment register.html", {"form": form})


def building_registration(request):
    form = B_R_F()

    return render(request, "Building register.html", {"form": form})

def get_BRF_form(request):
    if request.method =="POST":
        form = B_R_F(request.POST)
        if form.is_valid():
            try:
                connection = create_connection("db", "student", "123456", "localhost", "5432")
                query = f"""INSERT INTO data.buildings (building_names)
                            VALUES ('{B_R_F.Meta.model.Building_name}')"""
                executor(connection, query)
                form.save()
                return redirect("http://127.0.0.1:8000")
            except IntegrityError as intgrerr:
                return intgrerr
    return render(request, "Building register.html", {"form": form})


def cabinet_type_registration(request):
    form = C_T_R_F()

    return render(request, "Cabinet type register.html", {"form": form})

def get_CTRF_form(request):
    if request.method =="POST":
        form = C_T_R_F(request.POST)
        if form.is_valid():
            try:
                connection = create_connection("db", "student", "123456", "localhost", "5432")
                query = f"""INSERT INTO data.cabinet_types (cabinet_type_names)
                            VALUES ('{C_T_R_F.Meta.model.Cabinet_type_name}')"""
                executor(connection, query)
                form.save()
                return redirect("http://127.0.0.1:8000")
            except IntegrityError as intgrerr:
                return intgrerr
    return render(request, "Cabinet type register.html", {"form": form})


# Вторичные функции - создаются с использованием данных класса Data_container созданных первичными функциями

def cabinets_registration(request):  # Ожидает ввода клиентом Кабинета и данных о нём.
    if request.method =="POST":
        form = E_R_F(request.POST)
        if form.is_valid():
            try:
                connection = create_connection("db", "student", "123456", "localhost", "5432")
                query = f"""INSERT INTO data.cabinets (building, cabinet_number, cabinet_type, equipment)
                            VALUES ('{form.Building}', '{form.Cabinet_number}', '{form.Cabinet_type}', '{form.Equipment}');"""
                executor(connection, query)
                form.save()
                return redirect("http://127.0.0.1:8000")
            except IntegrityError as intgrerr:
                return intgrerr
    return render(request, "Cabinet register.html", {"form": form})


def descipline_full_info(request):
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
                  (teacher_name varchar(96) NOT NULL,
                  surname varchar(96) NOT NULL,
                  surname1 varchar(96) NOT NULL);"""       
        executor(connection, ttcq)
        dtcq = """CREATE TABLE IF NOT EXISTS data.disciplines
                  (discipline_names varchar(96) UNIQUE NOT NULL);"""
        executor(connection, dtcq)
        stcq = """CREATE TABLE IF NOT EXISTS data.subjects
                  (subject_names varchar(96) UNIQUE NOT NULL);"""
        executor(connection, stcq)
        btcq = """CREATE TABLE IF NOT EXISTS data.buildings
                  (building_names varchar(96) UNIQUE NOT NULL);"""
        executor(connection, btcq)
        cttcq = """CREATE TABLE IF NOT EXISTS data.cabinet_types
                   (cabinet_type_names varchar(96) UNIQUE NOT NULL);"""
        executor(connection, cttcq)
        ctcq = """CREATE TABLE IF NOT EXISTS data.cabinets
                  (building varchar(48) NOT NULL,
                  cabinet_number PRIMARY KEY integer NOT NULL,
                  cabinet_type varchar[3],
                  equipment varchar(96));"""
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