import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exercise.settings')

import django
django.setup()

from users.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_f_name = fakegen.first_name()
        fake_l_name = fakegen.last_name()
        fake_email = fakegen.email()
        user = User.objects.get_or_create(f_name=fake_f_name, l_name=fake_l_name,email=fake_email)[0]
        user.save()

if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('completed')