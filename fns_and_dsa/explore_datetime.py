from datetime import datetime
now = datetime.now()
print(now)

def display_current_datetime():
    now = datetime.datetime.now()
    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"The current date and time is: {current_date}")

def calculate_future_date(number_of_days):
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=number_of_days)  # Corrected line
    print(f"The date {number_of_days} days from now will be: {future_date.strftime('%Y-%m-%d %H:%M:%S')}")

display_current_datetime()

try:
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(number_of_days)
except ValueError:
    print("Please enter a valid integer number of days.")