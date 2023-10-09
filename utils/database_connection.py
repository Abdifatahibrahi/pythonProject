import sqlite3


class DatabaseConnection:
    def __int__(self):
        self.connection = None
        # self.host = host
    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect('data.db')
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb or exc_type or exc_val:
            self.connection.close()
        self.connection.commit()
        self.connection.close()
