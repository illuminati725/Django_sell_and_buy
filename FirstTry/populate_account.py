import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_try.settings')

import django
django.setup()

## FAKE POP SCRIPT
import random
from account.models import UserLoginDetails
from faker import Faker

fakegen=Faker()

def populate(N=10):
    fake_user_name_list=[
    'rishu1','rishu2','rishu3','rishu4','rishu5','rishu6','rishu7','rishu8','rishu9','rishu10','rishu11',
    ]
    for i in range(N):
        fake_fname=fakegen.first_name()
        fake_lname=fakegen.last_name()
        fake_user_name=fake_user_name_list[i]
        fake_phone_number=fakegen.phone_number()
        fake_address=fakegen.address()
        fake_city=fakegen.city()
        fake_country=fakegen.country()
        fake_password='123456789'
        fake_vpassword='123456789'

        UserAccount=UserLoginDetails.objects.get_or_create(
                                fname=fake_fname,
                                lname=fake_lname,
                                user_name=fake_user_name,
                                phone_number=fake_phone_number,
                                city=fake_city,
                                country=fake_country,
                                address=fake_address,
                                password=fake_password,
                                vpassword=fake_vpassword,
                                gender='male'
                                )[0]

if __name__=='__main__':
    print('populating script!')
    populate()
    print('populating complete!')
