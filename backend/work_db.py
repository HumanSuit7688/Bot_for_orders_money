import psycopg2
db_url = 'postgresql://ivan:D8pJaZh_yzpDXS4kFK1u6Q@cross-mantis-7154.7tc.cockroachlabs.cloud:26257/SpecBot?sslmode=verify-full'

class User():

    def __init__(self, tele_id):
        self.id = tele_id
        self.db_url = 'postgresql://ivan:D8pJaZh_yzpDXS4kFK1u6Q@cross-mantis-7154.7tc.cockroachlabs.cloud:26257/SpecBot?sslmode=verify-full'

    def return_role(self):
        conn = psycopg2.connect(self.db_url)
        cur = conn.cursor()

        cur.execute(f'SELECT role FROM users WHERE id = {self.id}')
        role = cur.fetchall()[0][0]

        return role

    def return_user_name(self):
        conn = psycopg2.connect(self.db_url)
        cur = conn.cursor()

        cur.execute(f'SELECT user_name FROM users WHERE id = {self.id}')
        user_name = cur.fetchall()[0][0]

        return user_name

    def return_wallet(self):
        conn = psycopg2.connect(self.db_url)
        cur = conn.cursor()

        cur.execute(f'SELECT wallet FROM users WHERE id = {self.id}')
        wallet = cur.fetchall()[0][0]

        return wallet

    def sign_up(self, user_name, role):
        conn = psycopg2.connect(self.db_url)
        cur = conn.cursor()

        cur.execute(f'INSERT INTO users (id, user_name, wallet, role) VALUES (%s, %s, %s, %s)', (self.id, user_name, 0.0, role))
        conn.commit()

    def check_log(self):
        conn = psycopg2.connect(self.db_url)
        cur = conn.cursor()

        cur.execute(f'SELECT * FROM users WHERE id = {self.id}')
        check = cur.fetchall()
        if check:
            return True
        else:
            return False

class Order():

    def __init__(self, id):
        self.id = id
        self.db_url = 'postgresql://ivan:D8pJaZh_yzpDXS4kFK1u6Q@cross-mantis-7154.7tc.cockroachlabs.cloud:26257/SpecBot?sslmode=verify-full'

    def insert_order_to_db(self, type, name, customer, work_amount):
        conn = psycopg2.connect(self.db_url)
        cur = conn.cursor()

        cur.execute('INSERT INTO orders (id, type, name, customer, work_amount) VALUES (%s, %s, %s, %s, %s)', (self.id, type, name, customer, work_amount))
        conn.commit()



def new_id_order():
    conn = psycopg2.connect(db_url)
    cur = conn.cursor()

    cur.execute('SELECT id FROM orders ORDER BY id desc;')
    last_id = cur.fetchall()[0][0]
    new_id = last_id + 1
    return new_id




new_id_order()
