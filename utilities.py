import datetime


def get_full_name():
	first_name = input("First name: ")
	last_name = input("Last name: ")
	return f"{last_name} {first_name}"


def get_age(BoY):
	today = datetime.date.today()
	return today.year - BoY
