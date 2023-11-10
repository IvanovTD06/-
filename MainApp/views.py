import pandas as pd

from os import mkdir
from os import error as os_error

from random import choice

from pathlib import Path

from django.shortcuts import render, redirect

from MainApp.forms import T_R_F, D_R_F, E_R_F, B_R_F, C_T_R_F, C_R_F, C_D


import psycopg2
from psycopg2.errors import OperationalError, DuplicateSchema, InvalidSchemaName

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
                       VALUES ('{form.cleaned_data.get("Name")}', '{form.cleaned_data.get("Surname")}', '{form.cleaned_data.get("Surname1")}');"""
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
                            VALUES ('{form.cleaned_data.get("Discipline_name")}')"""
                executor(connection, query)
                form.save()
                return redirect("http://127.0.0.1:8000")
            except AttributeError as atrerr:
                return atrerr,
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
                query = f"""INSERT INTO data.equipment (equipment_names)
                            VALUES ('{form.cleaned_data.get("Equipment_name")}');"""
                executor(connection, query)
                form.save()
                return redirect("http://127.0.0.1:8000")
            except AttributeError as atrerr:
                return atrerr
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
                            VALUES ('{form.cleaned_data.get("Building_name")}')"""
                executor(connection, query)
                form.save()
                return redirect("http://127.0.0.1:8000")
            except AttributeError as atrerr:
                return atrerr
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
                            VALUES ('{form.cleaned_data.get("Cabinet_type_name")}')"""
                executor(connection, query)
                form.save()
                return redirect("http://127.0.0.1:8000")
            except AttributeError as atrerr:
                return atrerr
    return render(request, "Cabinet type register.html", {"form": form})


# Вторичные функции - создаются с использованием данных класса Data_container созданных первичными функциями

def cabinet_registration(request):
    form = C_R_F()

    return render(request, "Cabinet register.html", {"form": form})

def get_CRF_form(request):
    if request.method =="POST":
        form = C_R_F(request.POST)
        if form.is_valid():
            try:
                connection = create_connection("db", "student", "123456", "localhost", "5432")
                query = f"""INSERT INTO data.cabinets (building, cabinet_number, cabinet_type, equipment)
                            VALUES ('{form.cleaned_data.get("Building")}', '{form.cleaned_data.get("Cabinet_number")}', '{form.cleaned_data.get("Cabinet_type")}',
                            '{form.cleaned_data.get("Equipment")}');"""
                executor(connection, query)
                form.save()
                return redirect("http://127.0.0.1:8000")
            except AttributeError as atrerr:
                return atrerr
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

    return f_i


# Третичные функции управляют данными вышестоящих функций


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

def registrate_connection(request):
    if request.method == "GET":
        form = C_D(request.GET)
        if form.is_valid():
            registred_connection = (form.cleaned_data.get())
            print(registred_connection)
            try:
                create_connection(registred_connection)
                return redirect("http://127.0.0.1:8000")
            except psycopg2.Error as error:
                return error
    return render(request, "htmldoc.html", {"db_form": form})



def executor(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

def reader(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
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
        etcq = """CREATE TABLE IF NOT EXISTS data.equipment
                  (equipment_names varchar(96) UNIQUE NOT NULL);"""
        executor(connection, etcq)
        btcq = """CREATE TABLE IF NOT EXISTS data.buildings
                  (building_names varchar(96) UNIQUE NOT NULL);"""
        executor(connection, btcq)
        cttcq = """CREATE TABLE IF NOT EXISTS data.cabinet_types
                   (cabinet_type_names varchar(96) UNIQUE NOT NULL);"""
        executor(connection, cttcq)
        ctcq = """CREATE TABLE IF NOT EXISTS data.cabinets
                  (building varchar(48) NOT NULL,
                  cabinet_number integer PRIMARY KEY NOT NULL,
                  cabinet_type varchar(96),
                  equipment varchar(96),
                  FOREIGN KEY (building) REFERENCES data.buildings (building_names),
                  FOREIGN KEY (cabinet_type) REFERENCES data.cabinet_types (cabinet_type_names),
                  FOREIGN KEY (equipment) REFERENCES data.equipment (equipment_names));"""
        executor(connection, ctcq)
        return render(request, "htmldoc.html")
    except DuplicateSchema as dserr:
        return render(request, "htmldoc.html", {"DSerr": dserr})

def db_drop_button(request):
    try:
        connection = create_connection("db", "student", "123456", "localhost", "5432")
        drop_database_query = "DROP SCHEMA data CASCADE;"
        ddb = executor(connection, drop_database_query)
        return render(request, "htmldoc.html", {"ddb": ddb})
    except InvalidSchemaName as dberr:
        return render(request, "htmldoc.html", {"ICNerr": dberr})

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



def main_page(request):
    form = C_D()

    return render(request, "htmldoc.html", {"db_form": form})
