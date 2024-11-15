import datetime


if __name__ == "__main__":
    # Access the `datetime` class using `datetime.datetime`
    current_time = datetime.datetime.now()
    print(current_time)  # Output: 2024-11-15 13:34:16.132869



    # 1. Working with `datetime`
    current_time = datetime.datetime.now()
    print("1.0 Current Date and Time:", current_time) # Output: 1.0 Current Date and Time: 2024-11-15 13:39:56.742475

    # Formatting the datetime
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print("1.1 Formatted Date and Time:", formatted_time) # Output: 1.1 Formatted Date and Time: 2024-11-15 13:39:56

    # Parsing a string into a datetime object
    date_str = "2024-11-10 14:30:00"
    '''
    parsed_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    
    Traceback (most recent call last):
        File "/home/ssr/Surendra/python_projects/core_python/core/import_modules/import_entire_module.py", line 21, in <module>
            parsed_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    AttributeError: module 'datetime' has no attribute 'strptime'
    '''
    parsed_time = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    print("1.2 Parsed Date and Time:", parsed_time) # Output: 1.2 Parsed Date and Time: 2024-11-10 14:30:00
