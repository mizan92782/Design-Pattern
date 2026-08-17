class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        #if alrady object initilize
        if self._initialized:
            return

        print("Initializing DB Connection...")
        self._initialized = True
    
    @classmethod
    def reset(cls):
        cls._instance = None
        
        
        
if __name__== "__main__":
    a=DatabaseConnection()
    b=DatabaseConnection()
    
    