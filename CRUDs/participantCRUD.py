import psycopg2

def insert(participant_id: int, phone: str, bday: str, full_name: str, dl_number: str, insurance_number: str, sex: str, treatment_needed: str,conn):
    cur = conn.cursor()
    cur.execute("INSERT INTO participant (participant_id, phone, bday, full_name, dl_number, insurance_number, sex, treatment_needed) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (participant_id, phone, bday, full_name, dl_number, insurance_number, sex, treatment_needed))
    conn.commit()
    cur.close()

def select(full_name: str, conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM participant WHERE full_name = (%s)", (full_name,))
    answer = cur.fetchall()
    return answer
    cur.close()

def select_all(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM participant ORDER BY participant_id")
    answer = cur.fetchall()
    return answer
    cur.close()

def update(participant_id: int, phone: str, bday: str, full_name: str, dl_number: str, insurance_number: str, sex: str, treatment_needed: str,conn):
    cur = conn.cursor()
    cur.execute("UPDATE participant SET participant_id = (%s), phone = (%s), bday = (%s), dl_number = (%s), insurance_number = (%s), sex = (%s), treatment_needed = (%s) WHERE full_name = (%s)", (participant_id, phone, bday, dl_number, insurance_number, sex, treatment_needed, full_name))
    conn.commit()
    cur.close()

def delete(full_name: str, conn):
    cur = conn.cursor()
    cur.execute("DELETE FROM participant WHERE full_name = (%s)", (full_name,))
    conn.commit()
    cur.close()