import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Users.settings")

import django
django.setup()

from app.models import User
from faker import Faker





fakegen = Faker()


def populate(n=5):
    for entry in range(n):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        # New entry
        _ = User.objects.get_or_create(
            first_name=fake_first_name,
            last_name=fake_last_name,
            email=fake_email)


if __name__ == '__main__':
    print("POPULATING DATABASES")
    populate(20)
    print("COMPLETES!")
