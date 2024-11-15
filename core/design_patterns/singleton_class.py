import threading

class SingletonClass:
    _instance = None  # Class attribute to store the single instance of SingletonClass

    def __new__(cls):
        if cls._instance is None:  # Check if an instance already exists
            '''
                    In following line, 
                1. super(SingletonClass, cls) returns a temporary proxy object of the object superclass 
                specifically bound to the cls class (which, in this case, is SingletonClass). SingletonClass is a 
                subclass of object (since all classes in Python implicitly inherit from object if no other superclass is specified).
                
                2. .__new__(cls) : 
                        Normally, when we create an instance of a class by calling SingletonClass(), Python first calls 
                    the __new__ method to allocate memory for the new object, and then it calls __init__ to initialize 
                    the object.
                    
                        Here, super(SingletonClass, cls).__new__(cls) calls the __new__ method of object (the base class of SingletonClass). 
                    This low-level operation is what actually creates the new instance of SingletonClass by allocating memory for it.
                        
                        We use super() here to make sure System should call super-class's __new__ method in place of 
                    overrided __new__ method of SingletonClass itself. and instead, we’re directly calling object.__new__ 
                    to allocate the memory for the new SingletonClass instance.
                    
                3. Finnaly: Once super(SingletonClass, cls).__new__(cls) is executed, we now have a fresh, newly allocated 
                    instance of SingletonClass. This instance doesn’t have any attributes yet initialized by __init__, 
                    but memory has been allocated for it.                    
            '''
            cls._instance = super(SingletonClass, cls).__new__(cls)  # Create new instance if none exists
        return cls._instance  # Return the single instance

    '''
        Why We Use __new__ Instead of __init__
        ======================================
            Normally, __init__ is called after an instance is created to initialize its attributes. However, __init__ 
        would be called every time SingletonClass() is called, potentially reinitializing the object repeatedly, 
        which would break the singleton behavior.
            Using __new__ allows us to intercept the instantiation process and ensure that only one instance is created. 
        We only allow super(SingletonClass, cls).__new__(cls) to be called once. After that, __new__ simply returns 
        the stored _instance without creating a new one.
            Putting It All Together:
                cls._instance = super(SingletonClass, cls).__new__(cls)      
                performs the following steps:
                1. Calls object.__new__(cls) through super(SingletonClass, cls) to create a new instance of SingletonClass 
                    without running __init__ or any custom initialization.
                2. Stores this new instance in cls._instance, the class-level variable that holds the one and only 
                    SingletonClass instance.
                3. This ensures that the next time SingletonClass() is called, __new__ will return the stored _instance, 
                    enforcing the singleton pattern.
            
    def __init__(self):
        pass
        
    '''


class ThreadSafeSingletonClass:
    _instance = None          # Holds the single instance of ThreadSafeSingletonClass
    _lock = threading.Lock()  # Class-level lock for thread safety

    def __new__(cls):
        if cls._instance is None:          # Check if an instance exists
            with cls._lock:                # Acquire the lock before creating the instance
                if cls._instance is None:  # Double-check within the lock
                    cls._instance = super(ThreadSafeSingletonClass, cls).__new__(cls)
        return cls._instance


def log_message(message):
    logger = ThreadSafeSingletonClass()




if __name__ == "__main__":

    obj1 = SingletonClass()
    obj2 = SingletonClass()
    is_equal_object = False
    if obj1 == obj2:
        is_equal_object = True

    print("is_equal_objectL ", is_equal_object)


    # Create multiple threads to test thread-safe singleton
    threads = [threading.Thread(target=log_message, args=(f"Log from thread {i}",)) for i in range(5)]

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()


