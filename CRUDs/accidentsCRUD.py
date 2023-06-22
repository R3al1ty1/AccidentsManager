import psycopg2

def insert(accident_id: int, conditions: str, accident_date: str, place: str, officer_id: int, city: str, conn):
    cur = conn.cursor()
    cur.execute("INSERT INTO accident (accident_id, conditions, accident_date, place, officer_id, city) VALUES (%s, %s, %s, %s, %s, %s)", (accident_id, conditions, accident_date, place, officer_id, city))
    conn.commit()
    cur.close()

def select(accident_date: str, place: str, conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM accident WHERE accident_date = (%s) AND place = (%s)", (accident_date,place))
    answer = cur.fetchall()
    return answer
    cur.close()

def select_all(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM accident ORDER BY accident_id")
    answer = cur.fetchall()
    return answer
    cur.close()

def update(accident_id: int, conditions: str, accident_date: str, place: str, officer_id: int, conn):
    cur = conn.cursor()
    cur.execute("UPDATE accident SET conditions = (%s), accident_date = (%s), place = (%s), officer_id = (%s) WHERE accident_id = (%s)", (conditions, accident_date, place, officer_id, accident_id))
    conn.commit()
    cur.close()

def delete(accident_id: int, conn):
    cur = conn.cursor()
    cur.execute("DELETE FROM accident WHERE accident_id = (%s)", (accident_id,))
    conn.commit()
    cur.close()