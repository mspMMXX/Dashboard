import mysql.connector


class DataBase:
    def __init__(self, host, user, password, database):
        """
        Initialisiert die Datenbankverbindung.
        :param host: der Hostname der Datenbank
        :param user: der Benutzername für die Datenbankverbindung
        :param password: das Passwort für die Datenbankverbindung
        :param database: der Name der Datenbank
        """
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor(
            dictionary=True)  # Verwenden eines Dict-Cursors für einfachere Abfrageergebnisse

    def execute_query(self, query, params=None):
        """
        Führt eine SQL-Abfrage aus.
        :param query: Die SQL-Abfrage, die ausgeführt werden soll
        :param params: optionale Parameter für die SQL-Abfrage
        """
        self.cursor.execute(query, params)
        # Wenn es sich um eine SELECT-Abfrage handelt, lesen Sie alle Ergebnisse
        if query.strip().upper().startswith('SELECT'):
            self.cursor.fetchall()  # Holen Sie sich alle Ergebnisse, um ungelesene Ergebnisse zu vermeiden
        self.connection.commit()  # Bestätigt die Transaktion

    def fetch_all(self, query, params=None):
        """
        Führt eine SQL-Abfrage aus und gibt alle Ergebnisse zurück.
        :param query: Die SQL-Abfrage, die ausgeführt werden soll
        :param params: optionale Parameter für die SQL-Abfrage
        :return: alle Zeilen, die der Abfrage entsprechen
        """
        self.cursor.execute(query, params)
        return self.cursor.fetchall()  # Gibt alle Ergebnisse zurück

    def fetch_one(self, query, params=None):
        """
        Führt eine SQL-Abfrage aus und gibt das erste Ergebnis zurück.
        :param query: Die SQL-Abfrage, die ausgeführt werden soll
        :param params: optionale Parameter für die SQL-Abfrage
        :return: die erste Zeile, die der Abfrage entspricht
        """
        self.cursor.execute(query, params)
        return self.cursor.fetchone()  # Gibt das erste Ergebnis zurück

    def close(self):
        """
        Schließt die Datenbankverbindung und den Cursor.
        """
        self.cursor.close()  # Schließt den Cursor
        self.connection.close()  # Schließt die Datenbankverbindung
