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
# cur.execute('DROP TABLE orders;')

# cur.execute('CREATE TABLE orders ('
#             'id INTEGER PRIMARY KEY,'
#             'type TEXT,'
#             'name TEXT,'
#             'customer INTEGER,'
#             'work_amount INTEGER'
#             ');')


# cur.execute(f'INSERT INTO orders (id, type, name, customer, work_amount) VALUES (%s, %s, %s, %s, %s)', (0, 'views', 'тест', 123456789, 0))

print('USERS')
cur.execute('SELECT * FROM users')
print(cur.fetchall())

print('ORDERS')
cur.execute('SELECT * FROM orders')
print(cur.fetchall())

conn.commit()