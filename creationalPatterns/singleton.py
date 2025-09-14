class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


# Example usage:
singleton1 = Singleton()
singleton2 = Singleton()

if __name__ == "__main__":
    print(singleton1 is singleton2)  # Output: True


class Database:
    _instance = None  # don't change this line
    connection = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.connection = cls._connect_to_database()
        return cls._instance

    @staticmethod
    def _connect_to_database():
        # Simulate a database connection setup
        return "Database Connection Established"


# Example usage:
db1 = Database()
db2 = Database()


if __name__ == "__main__":
    print(db1 is db2)  # Output: True
    print(db1.connection)  # Output: Database Connection Established
    print(db2.connection)  # Output: Database Connection Established
