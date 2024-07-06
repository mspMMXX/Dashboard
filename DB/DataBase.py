import mysql.connector

class DataBase:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        # Wenn es sich um eine SELECT-Abfrage handelt, lesen Sie alle Ergebnisse
        if query.strip().upper().startswith('SELECT'):
            self.cursor.fetchall()  # Holen Sie sich alle Ergebnisse, um ungelesene Ergebnisse zu vermeiden
        self.connection.commit()

    def fetch_all(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.connection.close()