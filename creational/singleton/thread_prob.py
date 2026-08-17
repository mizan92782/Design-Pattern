
# Multiple thread can run at a time and get instance =None,then create multiple instance 
# thats why use thread lock to  to run only one thred
import threading

class DBConnection:
    _instance  = None
    _lock =  threading.Lock()
    
    
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                print("Creating Databse connection......")
                cls._instance= super().__new__(cls)
        
        return cls._instance
    
    @classmethod
    def getDBConnection(cls):
        return cls._instance
    
    