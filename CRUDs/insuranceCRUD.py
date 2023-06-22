import psycopg2

def insert(insurance_id: int, insurance_name: str, accident_number: int, clients_number: int, rating: float, conn):
    cur = conn.cursor()
    cur.execute("INSERT INTO insurance (insurance_id, insurance_name, accident_number, clients_number, rating) VALUES (%s, %s, %s, %s, %s)", (insurance_id, insurance_name, accident_number, clients_number, rating))
    conn.commit()
    cur.close()

def select(insurance_name: str, conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM insurance WHERE insurance_name = (%s)", (insurance_name,))
    answer = cur.fetchall()
    return answer
    cur.close()

def select_all(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM insurance ORDER BY insurance_id")
    answer = cur.fetchall()
    return answer
    cur.close()

def update(insurance_id: int, insurance_name: str, accident_number: int, clients_number: int, rating: float, conn):
    cur = conn.cursor()
    cur.execute("UPDATE insurance SET insurance_id = (%s), accident_number = (%s), clients_number = (%s), rating = (%s) WHERE insurance_name = (%s)", (insurance_id, accident_number, clients_number, rating, insurance_name))
    conn.commit()
    cur.close()

def delete(insurance_name: str, conn):
    cur = conn.cursor()
    cur.execute("DELETE FROM insurance WHERE insurance_name = (%s)", (insurance_name,))
    conn.commit()
    cur.close()