
import datetime as dt
from datetime import datetime as dt2

if __name__ == "__main__":
    # Now you can directly use the `datetime` class
    current_time = dt2.now()
    print(current_time)  # Output: 2024-11-15 13:59:11.298839
    current_time = dt.datetime.now()
    print(current_time)  # Output: 2024-11-15 13:59:11.298854

# Output: 2024-11-15 13:59:11.298854


'''
from datetime import datetime
import datetime

if __name__ == "__main__":
    # Now you can directly use the `datetime` class
    current_time = datetime.now()
    print(current_time)  # Output: 2024-11-15 13:32:26.893499

Output: 
Traceback (most recent call last):
  File "/home/ssr/Surendra/python_projects/core_python/core/import_modules/import_module.py", line 6, in <module>
    current_time = datetime.now()
AttributeError: module 'datetime' has no attribute 'now'

'''