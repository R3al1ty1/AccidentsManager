import psycopg2

def insert(vehicle_id: int, motored: str, vehicle_name: str, color: str, brand: str, model: str, year_of_prod: str, vin: str, vehicle_passport: str, vehicle_registration: str, accident_number: int, insurance_id: int, damage_cost: int, conn):
    cur = conn.cursor()
    cur.execute("INSERT INTO vehicle (vehicle_id, motored, vehicle_name, color, brand, model, year_of_prod, vin, vehicle_passport, vehicle_registration, accident_number, insurance_id, damage_cost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (vehicle_id, motored, vehicle_name, color, brand, model, year_of_prod, vin, vehicle_passport, vehicle_registration, accident_number, insurance_id, damage_cost))
    conn.commit()
    cur.close()

def select(vin: str, conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM vehicle WHERE vin = (%s)", (vin,))
    answer = cur.fetchall()
    return answer
    cur.close()

def select_all(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM vehicle ORDER BY vehicle_id")
    answer = cur.fetchall()
    return answer
    cur.close()

def update(vehicle_id: int, motored: str, vehicle_name: str, color: str, brand: str, model: str, year_of_prod: str, vin: str, vehicle_passport: str, vehicle_registration:str, accident_number: int, insurance_id: int, damage_cost: int, conn):
    cur = conn.cursor()
    cur.execute("UPDATE vehicle SET vehicle_id = (%s), motored = (%s), vehicle_name = (%s), color = (%s), brand = (%s), model = (%s), year_of_prod = (%s), vehicle_passport= (%s), vehicle_registration = (%s), accident_number = (%s), insurance_id = (%s), damage_cost = (%s) WHERE vin = (%s)", (vehicle_id, motored, vehicle_name, color, brand, model, year_of_prod, vehicle_passport, vehicle_registration, accident_number, insurance_id, damage_cost, vin))
    conn.commit()
    cur.close()

def delete(vin: str, conn):
    cur = conn.cursor()
    cur.execute("DELETE FROM vehicle WHERE vin = (%s)", (vin,))
    conn.commit()
    cur.close()