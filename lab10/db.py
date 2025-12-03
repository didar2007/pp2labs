import psycopg2
from psycopg2.extras import RealDictCursor


def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="Snake",
        user="postgres",
        password="1357910didar",
        cursor_factory=RealDictCursor
    )

# Ищет пользователя в базе по имени
def get_user(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    conn.close()
    return user

# Создаёт нового пользователя и возвращает его user_id
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

# Сохраняет текущее состояние игры, т.е очки, уровень и положение змейки
def save_game_state(user_id, score, level, state_json):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO user_scores (user_id, score, level, snake_state, game_paused)
        VALUES (%s, %s, %s, %s, TRUE)
    """, (user_id, score, level, state_json))

    conn.commit()
    conn.close()

# Обновляет уровень пользователя в таблице users
def update_user_level(user_id, level):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE users SET level = %s WHERE user_id = %s",
        (level, user_id)
    )
    conn.commit()
    conn.close()

# Получает последнее сохранённое состояние игры пользователя
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
