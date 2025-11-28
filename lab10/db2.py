import psycopg2
import csv

# ---------------- ПОДКЛЮЧЕНИЕ ----------------
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="PhoneBook",  # имя вашей базы
        user="postgres",
        password="1357910didar"  # ваш пароль
    )

# ---------------- ВСТАВКА ----------------
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()
    conn.close()
    print("✅ Contact added")

def insert_from_csv(filename):
    conn = get_connection()
    cur = conn.cursor()
    with open(filename, newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
                (row['first_name'], row['phone'])
            )
    conn.commit()
    conn.close()
    print("✅ CSV uploaded")

# ---------------- ОБНОВЛЕНИЕ ----------------
def update_name(old_name, new_name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE phonebook SET first_name = %s WHERE first_name = %s",
        (new_name, old_name)
    )
    conn.commit()
    conn.close()
    print("✅ Name updated")

def update_phone(old_phone, new_phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE phonebook SET phone = %s WHERE phone = %s",
        (new_phone, old_phone)
    )
    conn.commit()
    conn.close()
    print("✅ Phone updated")

# ---------------- ЗАПРОСЫ ----------------
def show_all():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook")
    for row in cur.fetchall():
        print(row)
    conn.close()

def search_by_name(name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM phonebook WHERE first_name ILIKE %s",
        (f"%{name}%",)
    )
    for row in cur.fetchall():
        print(row)
    conn.close()

def search_by_phone(phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM phonebook WHERE phone = %s",
        (phone,)
    )
    print(cur.fetchone())
    conn.close()

# ---------------- УДАЛЕНИЕ ----------------
def delete_by_name(name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM phonebook WHERE first_name = %s",
        (name,)
    )
    conn.commit()
    conn.close()
    print("✅ Deleted by name")

def delete_by_phone(phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM phonebook WHERE phone = %s",
        (phone,)
    )
    conn.commit()
    conn.close()
    print("✅ Deleted by phone")
