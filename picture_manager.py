import sqlite3
import os
from picture import Picture


path = "imgs"
conn = sqlite3.connect('pictures.db')

c = conn.cursor()


def create_pictures_table():
    with conn:
        c.execute("""
        CREATE TABLE IF NOT EXISTS pictures(
        filename text PRIMARY KEY ,
        size INTEGER ,
        description text
        )
        """)


def create_people_table():
    with conn:
        c.execute("""
        CREATE TABLE IF NOT EXISTS people(
        id INTEGER PRIMARY KEY AUTOINCREMENT ,
        firstname text,
        middle_name text,
        lastname text,
        gender text,
        dob text,
        tlf text
        )""")


def create_people_picture_table():
    with conn:
        c.execute("""
                CREATE TABLE IF NOT EXISTS PeoplePicture (
                filename text REFERENCES pictures (filename),
                id INTEGER REFERENCES people (id),
                PRIMARY KEY (filename, id)
                )""")


def populate_pictures_table():
    for r, d, f in os.walk(path):
        for file in f:
            filepath = r+"/"+str(file)
            b = os.path.getsize(filepath)
            picture = Picture(str(file), b, None)
            insert_picture(picture)


def refresh_pictures_table():
    conn.row_factory = lambda cursor, row: row[0]
    ci = conn.cursor()
    database_filenames = ci.execute("""SELECT filename FROM pictures""").fetchall()
    for r, d, f in os.walk(path):
        for file in f:
            if file not in database_filenames:
                filepath = r+"/"+str(file)
                b = os.path.getsize(filepath)
                picture = Picture(str(file), b, None)
                insert_picture(picture)


def insert_picture(picture):
    with conn:
        c.execute("INSERT INTO pictures VALUES (:filename, :size, :description)",
                  {
                      'filename': picture.filename,
                      'size': picture.size,
                      'description': picture.description
                  })


def insert_person(person):
    with conn:
        c.execute("INSERT INTO people VALUES (Null, :firstname, :middle_name, :lastname, :gender, :dob, :tlf)",
                  {
                      'firstname': person.firstname,
                      'middle_name': person.middle_name,
                      'lastname': person.lastname,
                      'gender': person.gender,
                      'dob': person.dob,
                      'tlf': person.tlf
                  })


def show_table(table_name):
    with conn:
        sql = "SELECT * FROM " + table_name
        c.execute(sql)
        result = c.fetchall()
        for i in result:
            print(i)


def fill_people_in_pictures(picture_array, person_array):
    with conn:
        for filename in picture_array:
            for person_id in person_array:
                c.execute("INSERT INTO PeoplePicture VALUES (:filename, :id)",
                          {
                              'filename': filename,
                              'id': person_id
                          })


def fill_person_in_pictures(picture_array, person_id):
    with conn:
        for filename in picture_array:
            c.execute("INSERT INTO PeoplePicture VALUES (:filename, :id)",
                      {
                          'filename': filename,
                          'id': person_id
                      })


def fill_people_in_picture(filename, person_array):
    with conn:
        for person_id in person_array:
            c.execute("INSERT INTO PeoplePicture VALUES (:filename, :id)",
                      {
                          'filename': filename,
                          'id': person_id
                      })


def fill_person_in_picture(filename, person_id):
    with conn:
        c.execute("INSERT INTO PeoplePicture VALUES (:filename, :id)",
                  {
                      'filename': filename,
                      'id': person_id
                  })


def initial_setup():
    create_pictures_table()
    create_people_table()
    create_people_picture_table()
    # populate_pictures()



