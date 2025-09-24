from datetime import datetime
import calendar

def get_last_n_months_date_range(n, reference_date=None):
    if reference_date is None:
        reference_date = datetime.today()

    year = reference_date.year
    month = reference_date.month

    # Calculate the first month in the range
    start_month = month - n + 1
    start_year = year
    while start_month <= 0:
        start_month += 12
        start_year -= 1

    start_date = datetime(start_year, start_month, 1)

    # Last day of the current (reference) month
    last_day = calendar.monthrange(year, month)[1]
    end_date = datetime(year, month, last_day)

    lst_months = []
    current_year = start_date.year
    current_month = start_date.month
    while (current_year, current_month) <= (end_date.year, end_date.month):
        month_short = calendar.month_abbr[current_month]  # e.g., 'Jul'
        year_short = str(current_year)[-2:]  # Last two digits of year
        lst_months.append(f"{month_short}-{year_short}")

        # Move to next month
        current_month += 1
        if current_month > 12:
            current_month = 1
            current_year += 1
    print(", ".join(lst_months))

    return start_date.strftime('%d/%m/%Y'), end_date.strftime('%d/%m/%Y')


# Example Usage: Last 3 months including current month (assuming today is Sept 15, 2025)
start, end = get_last_n_months_date_range(3, reference_date=datetime(2025, 9, 15))
print(f"Date Range for Last 3 Months: {start} - {end}")


start, end = get_last_n_months_date_range(6, reference_date=datetime(2025, 9, 15))
print(f"Date Range for Last 6 Months: {start} - {end}")


start, end = get_last_n_months_date_range(3, reference_date=datetime(2026, 1, 15))
print(f"Date Range for Last 3 Months: {start} - {end}")

