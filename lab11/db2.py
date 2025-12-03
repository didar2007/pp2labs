import psycopg2
import csv
import json
from psycopg2.extras import RealDictCursor


def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="PhoneBook",
        user="postgres",
        password="1357910didar"
    )


def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL upsert_user(%s, %s)", (name, phone))
    conn.commit()
    conn.close()

    print("✅ Contact added/updated using procedure")


def insert_from_csv(filename):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    array_for_db = []

    with open(filename, newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            array_for_db.append({
                "first_name": row["first_name"],
                "phone": row["phone"]
            })

    js = json.dumps(array_for_db)

    cur.execute("SELECT * FROM insert_many_users(%s::jsonb)", (js,))
    bad_rows = cur.fetchall()

    conn.commit()
    conn.close()

    if bad_rows:
        print("\n⚠ Некорректные строки:")
        for r in bad_rows:
            print(r)
    else:
        print("✅ CSV imported successfully")


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


def show_all():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM phonebook ORDER BY id")
    rows = cur.fetchall()

    for r in rows:
        print(r)
    conn.close()


def search_by_name(name):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM search_by_pattern(%s)", (name,))
    rows = cur.fetchall()

    for r in rows:
        print(r)

    conn.close()


def search_by_phone(phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
    print(cur.fetchone())
    conn.close()


def delete_by_name(name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT delete_by_value(%s)", (name,))
    deleted = cur.fetchone()[0]

    conn.commit()
    conn.close()
    print(f"🗑 Deleted {deleted} rows")


def delete_by_phone(phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT delete_by_value(%s)", (phone,))
    deleted = cur.fetchone()[0]

    conn.commit()
    conn.close()
    print(f"🗑 Deleted {deleted} rows")


def get_page(limit, offset):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM get_phonebook_page(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    conn.close()
    return rows
