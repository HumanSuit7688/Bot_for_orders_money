import psycopg2

db_url = "postgresql://ivan:D8pJaZh_yzpDXS4kFK1u6Q@cross-mantis-7154.7tc.cockroachlabs.cloud:26257/SpecBot?sslmode=verify-full"

conn = psycopg2.connect(db_url)
cur = conn.cursor()

# cur.execute('CREATE TABLE users ('
#             'id INTEGER PRIMARY KEY,'
#             'user_name TEXT,'
#             'wallet REAL,'
#             'role TEXT'
#             ');')
#
# cur.execute('CREATE TABLE orders ('
#             'id INTEGER PRIMARY KEY,'
#             'type TEXT,'
#             'name TEXT,'
#             'work_amount INTEGER'
#             ');')


# cur.execute(f'INSERT INTO users (id, user_name, wallet, role) VALUES (%s, %s, %s, %s)', (1, name, 3.45, 'Z'))

print('USERS')
cur.execute('SELECT * FROM users')
print(cur.fetchall())

conn.commit()