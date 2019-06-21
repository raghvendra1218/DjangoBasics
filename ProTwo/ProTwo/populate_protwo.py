import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

## FAKE POP SCRIPT
from faker import Faker
from AppTwo.models import User

fake = Faker('hi_IN')

def populate(N = 5):

	for entry in range(N):
		#create fake data using fake instance of Faker
		fake_name = fake.name()
		fake_first_name, fake_last_name = fake_name.split(' ')
		fake_email = fake.email()

		# Create a new entry in user
		user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]


if __name__ == "__main__":
	print("Populating Database with fake users....")
	populate(5)
	print("Population completed.")