import psycopg2

def insert(officer_id: int, full_name: str, photo_path: str, bday: str, conn):
    cur = conn.cursor()
    cur.execute("INSERT INTO officer (officer_id, full_name, photo_path, bday) VALUES (%s, %s, %s, %s)", (officer_id, full_name, photo_path, bday))
    conn.commit()
    cur.close()

def select(full_name: str, conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM officer WHERE full_name = (%s)", (full_name,))
    answer = cur.fetchall()
    return answer
    cur.close()

def select_all(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM officer ORDER BY officer_id")
    answer = cur.fetchall()
    return answer
    cur.close()

def update(officer_id: int, full_name: str, photo_path: str, bday: str, conn):
    cur = conn.cursor()
    cur.execute("UPDATE officer SET officer_id = (%s), photo_path = (%s), bday = (%s) WHERE full_name = (%s)", (officer_id, photo_path, bday, full_name))
    conn.commit()
    cur.close()

def delete(full_name: str, conn):
    cur = conn.cursor()
    cur.execute("DELETE FROM officer WHERE full_name = (%s)", (full_name,))
    conn.commit()
    cur.close()