from datetime import datetime


def age_in_days(birthday):
    """Calculate the number of days a person has been living given a birthdate"""
    birthdate = datetime.strptime(birthday, "%Y-%m-%d")
    date_today = datetime.now()
    delta = date_today - birthdate
    days = delta.days
    print(f'I have been living for {days} days.')


my_birthday = "1988-10-31"
age_in_days(my_birthday)
