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


    # 2. Working with `timedelta`
    # Adding 7 days to the current time
    '''
    next_week = current_time + timedelta(days=7)
    
    Traceback (most recent call last):
      File "/home/ssr/Surendra/python_projects/core_python/core/import_modules/import_entire_module.py", line 35, in <module>
        next_week = current_time + timedelta(days=7)
    NameError: name 'timedelta' is not defined
    '''
    next_week = current_time + datetime.timedelta(days=7)
    print("2.0 Date and Time Next Week:", next_week) # Output: 2.0 Date and Time Next Week: 2024-11-22 13:39:56.742475

    # Subtracting 3 hours from the current time
    three_hours_ago = current_time - datetime.timedelta(hours=3)
    print("2.1 Date and Time 3 Hours Ago:", three_hours_ago) # Output: 2.1 Date and Time 3 Hours Ago: 2024-11-15 10:39:56.742475

    # Difference between two dates
    difference = parsed_time - current_time
    print("2.2 Difference Between Two Datetimes:", difference) # Output: 2.2 Difference Between Two Datetimes: -5 days, 0:50:03.257525



    # 3. Working with `date`
    # Getting today's date
    '''
    today = date.today()
    
    Traceback (most recent call last):
        File "/home/ssr/Surendra/python_projects/core_python/core/import_modules/import_entire_module.py", line 58, in <module>
        today = date.today()
    NameError: name 'date' is not defined
    '''
    today = datetime.date.today()
    print("3.0 Today's Date:", today) # Output: 3.0 Today's Date: 2024-11-15

    # Creating a specific date
    specific_date = datetime.date(2024, 12, 25)
    print("3.1 Specific Date:", specific_date) # Output: 3.1 Specific Date: 2024-12-25

    # Calculating the difference between two dates
    date_diff = specific_date - today
    print("3.2 Days Until Christmas:", date_diff.days) # Output: 3.2 Days Until Christmas: 40
