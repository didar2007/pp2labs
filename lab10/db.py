import psycopg2
from psycopg2.extras import RealDictCursor


# --- Подключение к базе ---
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="Snake",
        user="postgres",
        password="1357910didar",
        cursor_factory=RealDictCursor
    )


# --- Проверка, существует ли пользователь ---
def get_user(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    conn.close()
    return user


# --- Создание нового пользователя ---
def create_user(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
    "INSERT INTO users (username, level) VALUES (%s, %s) RETURNING user_id",
    (username, 1)
)
    user_id = cur.fetchone()['user_id']
    conn.commit()
    conn.close()
    return user_id


# --- Сохранение результата игры (например при паузе) ---
def save_game_state(user_id, score, level, state_json):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO user_scores (user_id, score, level, snake_state, game_paused)
        VALUES (%s, %s, %s, %s, TRUE)
    """, (user_id, score, level, state_json))

    conn.commit()
    conn.close()

def update_user_level(user_id, level):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE users SET level = %s WHERE user_id = %s",
        (level, user_id)
    )
    conn.commit()
    conn.close()


def get_last_save(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT score, level, snake_state
        FROM user_scores
        WHERE user_id = %s
        ORDER BY created_at DESC
        LIMIT 1
    """, (user_id,))
    data = cur.fetchone()
    conn.close()
    return data
