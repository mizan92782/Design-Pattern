class DatabaseConnection:

    # Store singleton instance
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating Database Connection...")
            cls._instance = super().__new__(cls)
            """here super() is object class,
            in python every class by default object class,her calling the parent class  __new methond to cratea a object of this class,which create + initialize object"""

        return cls._instance

    @classmethod
    def getDBConnection(cls):
        return DatabaseConnection()


if __name__ == "__main__":
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    print(db1 == db2)   # True
    print(db1 is db2)   # True

    print(id(db1))
    print(id(db2))