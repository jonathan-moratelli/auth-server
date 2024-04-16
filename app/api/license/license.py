from uuid import uuid4

from app.core.db.db import db_conn


def generate_new_license():
    key = uuid4()
    params = {"key": str(key)}
    cursor = db_conn.cursor()
    cursor.execute("INSERT INTO licenses(license_key) VALUES(:key)", params)
    db_conn.commit()
    cursor.close()
    
    return key


def get_licences(filter={}):
    licenses = []
    params = {}
    cursor = db_conn.cursor()
    query = "SELECT license_key, machine_id, created_at, updated_at FROM licenses"
    if filter:
        query += " WHERE "
        for k in filter.keys():
            query += f"{k} = :{k} "
            params[k] = filter[k]
    print(query)
    result = cursor.execute(query, params)
    for row in result:
        licenses.append({
            "licence_key": row[0],
            "machine_id": row[1],
            "created_at": row[2],
            "updated_at": row[3],
        })
    cursor.close()
    
    return licenses
