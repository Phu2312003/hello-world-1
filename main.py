from utilities import get_age


if __name__ == '__main__':
	print('Hello, world!')
	birth_of_year = int(input('BoY: '))
	print(f"Your age: {get_age(birth_of_year)}")
