# @dn- Danal storage related functionalities

# 데이터베이스에 데이터를 저장하고 관리하는 모듈

import sqlite3

# 데이터 저장소 클래스
class DNStorage:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def dn_create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.cursor.execute(query)
        self.conn.commit()

    def dn_insert_data(self, table_name, data):
        placeholders = ', '.join(['?' for _ in range(len(data))])
        query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        self.cursor.execute(query, data)
        self.conn.commit()

    def dn_get_data(self, table_name, condition=None):
        query = f"SELECT * FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def dn_delete_data(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.cursor.execute(query)
        self.conn.commit()

    def dn_close_connection(self):
        self.conn.close()

# 테스트용 코드
if __name__ == '__main__':
    storage = DNStorage('example.db')
    storage.dn_create_table('users', 'id INTEGER PRIMARY KEY, name TEXT, age INTEGER')
    storage.dn_insert_data('users', (1, 'Alice', 30))
    storage.dn_insert_data('users', (2, 'Bob', 25))
    print(storage.dn_get_data('users'))
    storage.dn_delete_data('users', 'name="Alice"')
    print(storage.dn_get_data('users'))
    storage.dn_close_connection()
            

# 이와 같은 방식으로 Danal 회사의 storage 관련 Python 파일을 작성할 수 있습니다.